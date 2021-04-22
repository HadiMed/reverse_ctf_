# Write up 

[![Maintenance](https://img.shields.io/badge/Hard-200points-red.svg)](https://bitbucket.org/lbesson/ansi-colors)

<b> Description :</b> <br/> 
<i>We discovered this tool in the E.T. toolkit which they used to encrypt and exfiltrate files from infected systems. Can you help us recover the files?
This challenge will raise 43 euros for a good cause.</i> <br/>  <br/>

so its an encryptor , the purpose is to decrypt the pdf encrypted with this program <br/>
# Reversing
diving into the executable , first its using a  <b>TLSCallback </b> (old anti debugging technique ) to execute the code before the entry point , it will try to load a ressource named (BIN ) from the ressource section and decrypt it with some shifting operations <br/><br/>
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
this ressouce is a dll called XuTav.dll that contains the encyption function , the program will call <b> GetProcAddress </b> with the argument <b>EncryptFiles <b/> ,after that it will call the EncryptFiles to encrypt all files under <b> C:\Users\username\Docs\*  </b> , its using <b> AES-128 </b> with a key derived from a hash base data <br/>
```assembly 
mov     r8, [rsp+140h+phHash]
lea     rax, [rsp+140h+phKey]
mov     rcx, [rsp+140h+phProv] ; hProv
xor     r9d, r9d        ; dwFlags
mov     edx, 660Eh      ; Algid
mov     qword ptr [rsp+140h+dwCreationDisposition], rax ; phKey
call    cs:CryptDeriveKey

 ```
