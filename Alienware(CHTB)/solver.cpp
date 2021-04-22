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
