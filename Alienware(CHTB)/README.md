# Write up 

[![Maintenance](https://img.shields.io/badge/medium-325points-green.svg)](https://bitbucket.org/lbesson/ansi-colors)

<b> Description :</b> <br/> 
<i>We discovered this tool in the E.T. toolkit which they used to encrypt and exfiltrate files from infected systems. Can you help us recover the files?
This challenge will raise 43 euros for a good cause.</i> <br/>  <br/>

so its an encryptor , the purpose is to decrypt the pdf encrypted with this program <br/>
# Reversing
diving into the executable , first its using a  <b>TLSCallback </b> (old anti debugging technique ) to execute the code before the entry point , it will try to load a ressource named (BIN ) from the ressource section and unpack it with some shifting operations : <br/><br/>
```assembly
               mov     [r11+8], rbx
                lea     r8, Type ; "BIN"
                mov     [r11+10h], rbp
                mov     edx, 66h ; lpName
                mov     [r11+18h], rsi
                xor     ecx, ecx ; hModule
                mov     [r11-8], rdi
                call    cs:FindResourceW
                mov     rdx, rax ; hResInfo
                xor     ecx, ecx ; hModule
                mov     rbx, rax
                call    cs:LoadResource
                mov     rdx, rbx ; hResInfo
                xor     ecx, ecx ; hModule
                mov     rdi, rax
                call    cs:SizeofResource
                mov     rcx, rdi ; hResData
                mov     esi, eax
                call    cs:LockResource
                mov     r9d, 4 ; flProtect
                mov     r8d, 1000h ; flAllocationType
                mov     edx, esi ; dwSize
                xor     ecx, ecx ; lpAddress
                mov     rbx, rax
                call    cs:VirtualAlloc
                xor     r9d, r9d
                mov     rdi, rax
                test    esi, esi
```
<br/>
this ressouce is a dll called <b> XuTav.dll</b> that contains the encyption function , the program will call <b> GetProcAddress </b> with the argument <b>EncryptFiles </b> ,after that it will call the EncryptFiles to encrypt all files under <b> C:\Users\username\Docs\*  </b> , its using <b> AES-128 </b> with a key derived from a hash base data <br/> :
  
```assembly 
mov     r8, [rsp+140h+phHash]
lea     rax, [rsp+140h+phKey]
mov     rcx, [rsp+140h+phProv] ; hProv
xor     r9d, r9d        ; dwFlags
mov     edx, 660Eh      ; Algid
mov     qword ptr [rsp+140h+dwCreationDisposition], rax ; phKey
call    cs:CryptDeriveKey

 ```
 
 then on each iteration it will read 48 byte from the file with the API <b> ReadFile </b> :
 
 ```assembly
 xor     eax, eax
mov     [rsp+140h+NumberOfBytesRead], r12d
xor     edx, edx        ; lpFileSizeHigh
mov     qword ptr [rsp+140h+Dest], rax
mov     rcx, r14        ; hFile
mov     [rsp+140h+var_D0], rax
mov     [rsp+140h+var_C8], rax
mov     ebx, r12d
mov     qword ptr [rbp+70h+NumberOfBytesWritten], rax
mov     edi, r12d
mov     [rbp+70h+phHash], rax
mov     [rbp+70h+phKey], rax
call    cs:GetFileSize
lea     r9, [rsp+140h+NumberOfBytesRead] ; lpNumberOfBytesRead
mov     qword ptr [rsp+140h+dwCreationDisposition], r12 ; lpOverlapped
mov     r8d, 30h        ; nNumberOfBytesToRead
lea     rdx, [rsp+140h+Dest] ; lpBuffer
mov     rcx, r14        ; hFile
mov     r15d, eax
call    cs:ReadFile
test    eax, eax
jz      loc_1800014D3
```

and encypt with <b>CryptEncrypt</b> : 
```assembly 
add     edi, ecx
mov     dword ptr [rsp+140h+hTemplateFile], 30h ; dwBufLen
mov     rcx, [rsp+140h+phKey] ; hKey
lea     rax, [rsp+140h+NumberOfBytesRead]
mov     qword ptr [rsp+140h+dwFlagsAndAttributes], rax ; pdwDataLen
cmp     edi, r15d
lea     rax, [rsp+140h+Dest]
cmovz   ebx, r13d
mov     qword ptr [rsp+140h+dwCreationDisposition], rax ; pbData
mov     r8d, ebx        ; Final
xor     r9d, r9d        ; dwFlags
xor     edx, edx        ; hHash
call    cs:CryptEncrypt
test    eax, eax
```
After that it will remove the old file "Confidential.pdf" and replace it with "Confidential.pdf.alien" . 

# Solver 

Just using the API CryptDecrypt to recover the file 

```c++
#include <iostream>
#include <stdio.h>
#include <Windows.h>
#include <stdlib.h>

int main()
{
   
    char  Dest[] = {0x2F, 0x6B , 0x18 , 0xE4 , 0x9A , 0x33 ,0xD9 , 0xC7 ,0xA0 , 0x31 , 0x46 , 0x1F , 0x16 , 0x66 , 0x19 , 0xF7};

    wchar_t  Ddes[0x10]; 
    
    mbstowcs(Ddes, Dest, 0x10); 

   
    HCRYPTPROV phProve;
    
    HCRYPTHASH pHash;
    HCRYPTKEY phKey;

    

    HANDLE readd = CreateFileA("C:\\Users\\Slashroot\\source\\repos\\solver\\Debug\\Conf", 0x80000000, 1, 0, 3, 0x80000000, 0);
    

    HANDLE writ = CreateFileA("C:\\Users\\Slashroot\\source\\repos\\solver\\Debug\\flag.pdf", 0x40000000, 1, 0, 1, 0x80, 0);

    LPCSTR zsProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider"; 
    

    if(!CryptAcquireContextA(&phProve, NULL ,zsProvider , PROV_RSA_AES, 0xF0000000))
        exit(0);
    
     
    if (!CryptCreateHash(phProve, 0x800C, 0, 0, &pHash)) 
        exit(0); 
    
    
     if(!CryptHashData(pHash, (const BYTE*)Ddes, 0x10, 0)) 
         exit(0);
     
     
    
    if(!CryptDeriveKey(phProve, 0x660E, pHash, 0x10, &phKey)) 
        exit(0);
    
    

    DWORD Numberofbytes;

    BOOL final=FALSE; 

    int size=0; 

    DWORD Numberofbyteswritten = 0x30 ; 

    BYTE  * Dest2 = (BYTE*)malloc(0x30) ; 

    


    for (int i = GetFileSize(readd, NULL); ReadFile(readd, Dest2, 0x30, &Numberofbytes, NULL);) {
       
        
        if (!Numberofbytes) break; 
        size += Numberofbytes; 

        if (size == i) final = TRUE; 


        
        if(!CryptDecrypt(phKey, NULL, final, 0, Dest2, &Numberofbytes)) exit(0); 
        
            
       
        
        WriteFile(writ, Dest2,0x30, &Numberofbytes, 0); 

}
    
    CryptReleaseContext(phProve, 0); 
    CryptDestroyKey(phKey); 
    CryptDestroyHash(pHash); 
    CloseHandle(writ); 
    CloseHandle(readd); 

    }
 ```
 <b>End.</b>




