## RunPe process hollowing
### Intro 
- this technique is one of the most used techniques on code injection category , the basic idea is start a new process on a suspended state , a trusted process , lets say something like ***explorer.exe*** , then it will  unmap it's section with ```NtUnmapViewOfSection``` , remap all of the target process sections with valid sections using ```WriteProcessMemory``` from kernel32.dll , to hide this functionality malware will probably try to resolve this address passing by the ```TEB->PEB->Ldr->InMemoryOrderLoadList->currentProgram->ntdll->kernel32.BaseDll ``` same thing for ```NtUnmapViewOfSection``` passing by ntdll , then it will set thread context of the remote thread , and call ResumeThread .
### Example 
This is an example of a runPe , this will just start itself as a new process , decrypt a payload and copy it to the new created process , to have an idea of the code (it's just resolving base addresses of kernel32.dll then writeprocessmemeory , createprocess32 , setthreadcontext , resumethread)

- resolving base address : 
```asm
UPX0:00402B90 mov     eax, 30h
UPX0:00402B95 mov     edx, fs:[eax]
UPX0:00402B98 mov     edx, [edx+0Ch]
UPX0:00402B9B mov     edx, [edx+14h]
UPX0:00402B9E mov     edi, [edx+28h]
UPX0:00402BA1 xor     eax, eax
UPX0:00402BA3 mov     ecx, 200h
UPX0:00402BA8 repne scasw
UPX0:00402BAB push    edi
UPX0:00402BAC mov     ecx, 200h
UPX0:00402BB1 repne scasw
UPX0:00402BB4 mov     eax, 200h
UPX0:00402BB9 sub     eax, ecx
UPX0:00402BBB pop     esi
UPX0:00402BBC lea     edi, [ebp+314h]
UPX0:00402BC2 mov     ecx, eax
UPX0:00402BC4
UPX0:00402BC4 loc_402BC4:                             ; CODE XREF: start:loc_402BCBj
UPX0:00402BC4 lodsw
UPX0:00402BC6 cmp     al, 22h
UPX0:00402BC8 jz      short loc_402BCB
UPX0:00402BCA stosb
UPX0:00402BCB
UPX0:00402BCB loc_402BCB:                             ; CODE XREF: start-3AEj
UPX0:00402BCB loop    loc_402BC4
UPX0:00402BCD jmp     loc_402CB0
```
- resolving address of function 

```asm
UPX0:00402BD2 push    ebp
UPX0:00402BD3 mov     ebp, esp
UPX0:00402BD5 mov     ebx, large fs:30h
UPX0:00402BDC mov     ebx, [ebx+0Ch]
UPX0:00402BDF mov     ebx, [ebx+14h]
UPX0:00402BE2 mov     edx, [ebx+4]
UPX0:00402BE5 xor     ecx, ecx
UPX0:00402BE7 xor     eax, eax
UPX0:00402BE9 jmp     short loc_402BEF
UPX0:00402BEB ; ---------------------------------------------------------------------------
UPX0:00402BEB
UPX0:00402BEB loc_402BEB:                             ; CODE XREF: sub_402BD2+42j
UPX0:00402BEB cmp     ebx, edx
UPX0:00402BED jz      short loc_402C1B
UPX0:00402BEF
UPX0:00402BEF loc_402BEF:                             ; CODE XREF: sub_402BD2+17j
UPX0:00402BEF mov     esi, [ebx+28h]
UPX0:00402BF2
UPX0:00402BF2 loc_402BF2:                             ; CODE XREF: sub_402BD2+31j
UPX0:00402BF2 lodsw
UPX0:00402BF4 test    al, al
UPX0:00402BF6 jz      short loc_402C05
UPX0:00402BF8 cmp     al, 60h
UPX0:00402BFA jbe     short loc_402BFE
UPX0:00402BFC sub     al, 20h
UPX0:00402BFE
UPX0:00402BFE loc_402BFE:                             ; CODE XREF: sub_402BD2+28j
UPX0:00402BFE xor     cl, al
UPX0:00402C00 rol     ecx, 18h
UPX0:00402C03 jmp     short loc_402BF2
UPX0:00402C05 ; ---------------------------------------------------------------------------
UPX0:00402C05
UPX0:00402C05 loc_402C05:                             ; CODE XREF: sub_402BD2+24j
UPX0:00402C05 cmp     ecx, [ebp+arg_0]
UPX0:00402C08 jz      short loc_402C16
UPX0:00402C0A mov     ecx, 0
UPX0:00402C0F mov     ebx, [ebx]
UPX0:00402C11 mov     esi, [ebx+4]
UPX0:00402C14 jmp     short loc_402BEB
UPX0:00402C16 ; ---------------------------------------------------------------------------
UPX0:00402C16
UPX0:00402C16 loc_402C16:                             ; CODE XREF: sub_402BD2+36j
UPX0:00402C16 mov     eax, [ebx+10h]
UPX0:00402C19 jmp     short loc_402C20
UPX0:00402C1B ; ---------------------------------------------------------------------------
UPX0:00402C1B
UPX0:00402C1B loc_402C1B:                             ; CODE XREF: sub_402BD2+1Bj
UPX0:00402C1B mov     eax, 0
UPX0:00402C20
UPX0:00402C20 loc_402C20:                             ; CODE XREF: sub_402BD2+47j
UPX0:00402C20 mov     esp, ebp
UPX0:00402C22 pop     ebp
UPX0:00402C23 retn    4
```
this blocks repeats (the calls of eax) all the functions pointers gets stored in eax <br/> <br/>
![hibou](https://user-images.githubusercontent.com/57273771/144335020-ebd7d479-acc3-45ff-8b9c-b2ce839718de.png)

- we can just break on the last call to ResumeThread , and use a tool called ```pd``` to dump executable from memory of the new created process (it will fix the IAT ) from there it's plain vanilla to find the flag
