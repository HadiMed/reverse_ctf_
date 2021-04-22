# Write up 

[![Maintenance](https://img.shields.io/badge/Hard-200points-red.svg)](https://bitbucket.org/lbesson/ansi-colors)

<b> Description :</b> <br/> 
<i>We discovered this tool in the E.T. toolkit which they used to encrypt and exfiltrate files from infected systems. Can you help us recover the files?
This challenge will raise 43 euros for a good cause.</i> <br/> 

so its an encryptor , the purpose is to decrypt the pdf encrypted with this program <br/>
<b> Reversing :</b> <br/> 
diving into the executable , first its using a  <b>TLSCallback </b> (old anti debugging technique ) to execute the code before the entry point , it will try to load a ressource named (BIN ) from the ressource section and decrypt it with some shifting operations <br/>
<img src="BIN.png"/>
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
