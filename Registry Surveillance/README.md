## Write up 
[![Maintenance](https://img.shields.io/badge/hard-200points-red.svg)](https://bitbucket.org/lbesson/ansi-colors)

- We are in the possesion of a PE file , in the beginning some checks are done to ensure that we are running on some  specific windows version (probably XP or older) , since windows patched version 7 to not allow external not signed drivers to be loaded but we will get to that later .. 
- anyway the important functionality start here :
```asm
mov     eax, ds:dword_10C31D0
mov     edx, offset aEvil_payload ; "EVIL_PAYLOAD"
mov     [ecx], eax
mov     eax, ds:dword_10C31D4
mov     [ecx+4], eax
mov     eax, ds:dword_10C31D8
mov     [ecx+8], eax
mov     ax, ds:word_10C31DC
mov     [ecx+0Ch], ax
mov     al, ds:byte_10C31DE
push    ebx
push    edi
mov     [ecx+0Eh], al
lea     ecx, [ebp+pcbBytesNeeded]
push    6Bh
call    sub_10C1310
mov     edx, [ebp+pcbBytesNeeded]
lea     ecx, [ebp+Buffer]
push    ecx             ; lpFileName
mov     ecx, eax        ; Str
call    sub_10C1290
push    6Ch
mov     edx, offset aEvil_driver ; "EVIL_DRIVER"
lea     ecx, [ebp+pcbBytesNeeded]
call    sub_10C1310
mov     edx, [ebp+pcbBytesNeeded]
lea     ecx, [ebp+FileName]
push    ecx             ; lpFileName
mov     ecx, eax        ; Str
call    sub_10C1290
push    Memory          ; Memory
call    ds:free
add     esp, 14h
lea     edx, [ebp+FileName]
call    sub_10C1000
mov     esi, eax
cmp     esi, 0FFFFFFFFh
jz      loc_10C15C5
```
- this piece of code will load 2 ressources from the .rsrc section base64 encoded , the first one is another executable called ***"VERIFIER.exe"*** , the other is a driver named ***"EVIL_DRIVER.sys"*** , after that a service is created to run the driver , another process is created the VERIFER.exe , this executable will check if a specific input respect some XOR operations in the following manner : 
```asm 
text:00401041                 mov     ebp, esp
.text:00401043                 sub     esp, 68h
.text:00401046                 mov     eax, ___security_cookie
.text:0040104B                 xor     eax, ebp
.text:0040104D                 mov     [ebp+var_4], eax
.text:00401050                 push    offset aHelloFromTheUs ; "Hello from the userland, Do you have th"...
.text:00401055                 call    sub_401010
.text:0040105A                 lea     eax, [ebp+Buffer]
.text:0040105D                 push    eax             ; Buffer
.text:0040105E                 call    ds:gets
.text:00401064                 lea     ecx, [ebp+Buffer]
.text:00401067                 add     esp, 8
.text:0040106A                 lea     edx, [ecx+1]
.text:0040106D                 nop     dword ptr [eax]
.text:00401070
.text:00401070 loc_401070:                             ; CODE XREF: sub_401040+35j
.text:00401070                 mov     al, [ecx]
.text:00401072                 inc     ecx
.text:00401073                 test    al, al
.text:00401075                 jnz     short loc_401070
.text:00401077                 sub     ecx, edx
.text:00401079                 cmp     ecx, 17h
.text:0040107C                 jnz     loc_40117C
.text:00401082                 mov     al, [ebp+Buffer]
.text:00401085                 xor     al, 1
.text:00401087                 cmp     al, 55h
.text:00401089                 jnz     loc_40117C
.text:0040108F                 mov     al, [ebp+var_67]
.text:00401092                 xor     al, 2
.text:00401094                 cmp     al, 4Fh
.text:00401096                 jnz     loc_40117C
.text:0040109C                 mov     al, [ebp+var_66]
.text:0040109F                 xor     al, 3
.text:004010A1                 cmp     al, 78h
.text:004010A3                 jnz     loc_40117C
.text:004010A9                 mov     al, [ebp+var_65]
.text:004010AC                 xor     al, 4
.text:004010AE                 cmp     al, 4Fh
.text:004010B0                 jnz     loc_40117C
.text:004010B6                 mov     al, [ebp+var_64]
.text:004010B9                 xor     al, 5
.text:004010BB                 cmp     al, 36h
.text:004010BD                 jnz     loc_40117C
.text:004010C3                 mov     al, [ebp+var_63]
.text:004010C6                 xor     al, 6
.text:004010C8                 cmp     al, 74h
.text:004010CA                 jnz     loc_40117C
.text:004010D0                 mov     al, [ebp+var_62]
.text:004010D3                 xor     al, 7
.text:004010D5                 cmp     al, 69h
.text:004010D7                 jnz     loc_40117C
.text:004010DD                 mov     al, [ebp+var_61]
.text:004010E0                 xor     al, 8
.text:004010E2                 cmp     al, 3Bh
.text:004010E4                 jnz     loc_40117C
.text:004010EA                 mov     al, [ebp+var_60]
.text:004010ED                 xor     al, 9
.text:004010EF                 cmp     al, 38h
.text:004010F1                 jnz     loc_40117C
.text:004010F7                 mov     al, [ebp+var_5F]
.text:004010FA                 xor     al, 0Ah
.text:004010FC                 cmp     al, 55h
.text:004010FE                 jnz     short loc_40117C
.text:00401100                 mov     al, [ebp+var_5E]
.text:00401103                 xor     al, 0Bh
.text:00401105                 cmp     al, 5Fh
.text:00401107                 jnz     short loc_40117C
.text:00401109                 mov     al, [ebp+var_5D]
.text:0040110C                 xor     al, 0Ch
.text:0040110E                 cmp     al, 3Dh
.text:00401110                 jnz     short loc_40117C
.text:00401112                 mov     al, [ebp+var_5C]
.text:00401115                 xor     al, 0Dh
.text:00401117                 cmp     al, 6Eh
.text:00401119                 jnz     short loc_40117C
.text:0040111B                 mov     al, [ebp+var_5B]
.text:0040111E                 xor     al, 0Eh
.text:00401120                 cmp     al, 65h
.text:00401122                 jnz     short loc_40117C
.text:00401124                 mov     al, [ebp+var_5A]
.text:00401127                 xor     al, 0Fh
.text:00401129                 cmp     al, 3Ch
.text:0040112B                 jnz     short loc_40117C
.text:0040112D                 mov     al, [ebp+var_59]
.text:00401130                 xor     al, 10h
.text:00401132                 cmp     al, 64h
.text:00401134                 jnz     short loc_40117C
.text:00401136                 mov     al, [ebp+var_58]
.text:00401139                 xor     al, 11h
.text:0040113B                 cmp     al, 4Eh
.text:0040113D                 jnz     short loc_40117C
.text:0040113F                 mov     al, [ebp+var_57]
.text:00401142                 xor     al, 12h
.text:00401144                 cmp     al, 4Dh
.text:00401146                 jnz     short loc_40117C
.text:00401148                 mov     al, [ebp+var_56]
.text:0040114B                 xor     al, 13h
.text:0040114D                 cmp     al, 43h
.text:0040114F                 jnz     short loc_40117C
.text:00401151                 mov     al, [ebp+var_55]
.text:00401154                 xor     al, 14h
.text:00401156                 cmp     al, 20h
.text:00401158                 jnz     short loc_40117C
.text:0040115A                 mov     al, [ebp+var_54]
.text:0040115D                 xor     al, 15h
.text:0040115F                 cmp     al, 66h
.text:00401161                 jnz     short loc_40117C
.text:00401163                 mov     al, [ebp+var_53]
.text:00401166                 xor     al, 16h
.text:00401168                 cmp     al, 45h
.text:0040116A                 jnz     short loc_40117C
.text:0040116C                 mov     al, [ebp+var_52]
.text:0040116F                 xor     al, cl
.text:00401171                 cmp     al, 6Ah
.text:00401173                 jnz     short loc_40117C
.text:00401175                 mov     ecx, 1
.text:0040117A                 jmp     short loc_40117E
```
- when we supply the right input which is ***TM{K3rn31_T1ck3t__P4sS}*** , we get this output : ***Welldone, you have the valid one, this is your key in the KERNEL-LAND, your secret is hidden somewhere there GoodLuck !!***
## reversing the driver 
- I was waiting for some IRP requests to be done , this driver hooks ZwQueryinformation and some other function , save some CPU state , change the value on CR3 (Vmem) and some things , but this is all deceiving  actually our flag will be decrypted on this function :
```c
void sub_40149C()
{
  signed int v0; // edx@2
  int v1; // ecx@2
  int v2; // ebx@6
  int v3; // eax@6
  unsigned int v4; // eax@12
  STRING DestinationString; // [sp+0h] [bp-6Ch]@1
  char v6[48]; // [sp+8h] [bp-64h]@6
  wchar_t v7[2]; // [sp+38h] [bp-34h]@9
  int v8; // [sp+3Ch] [bp-30h]@9
  int v9; // [sp+40h] [bp-2Ch]@9
  int v10; // [sp+44h] [bp-28h]@9
  wchar_t v11[2]; // [sp+48h] [bp-24h]@9
  int v12; // [sp+4Ch] [bp-20h]@9
  int v13; // [sp+50h] [bp-1Ch]@9
  int v14; // [sp+54h] [bp-18h]@9
  int v15; // [sp+58h] [bp-14h]@9
  int v16; // [sp+5Ch] [bp-10h]@9
  int v17; // [sp+60h] [bp-Ch]@9
  __int16 v18; // [sp+64h] [bp-8h]@9

  if ( RtlUnicodeStringToAnsiString(&DestinationString, SourceString, 1u) >= 0 )
  {
    v0 = 0;
    v1 = 0;
    while ( *((_BYTE *)&word_4019F2 + v1) == DestinationString.Buffer[v1] )
    {
      ++v1;
      if ( v1 == 15 )
      {
        if ( dword_4031A4 == 2 )
        {
          v2 = dword_4031A0 + 12;
          qmemcpy(v6, &word_401A02, sizeof(v6));
          v3 = wcscmp((const unsigned __int16 *)(dword_4031A0 + 12), (const unsigned __int16 *)v6);
          if ( v3 )
            v3 = -(v3 < 0) | 1;
          if ( v3 )
          {
            qmemcpy(v11, "W", 0x1Cu);
            v4 = *(_DWORD *)(dword_4031A0 + 8);
            if ( v4 <= 0x1C )
            {
              wcsncpy((wchar_t *)v2, v11, (v4 >> 1) - 1);
            }
            else
            {
              wcsncpy((wchar_t *)v2, v11, 0xEu);
              *(_WORD *)(v2 + 28) = 0;
            }
          }
          else
          {
            *(_DWORD *)v7 = 0;
            v8 = 0;
            v9 = 0;
            v10 = 0;
            *(_DWORD *)v11 = 0;
            v12 = 0;
            v13 = 0;
            v14 = 0;
            v15 = 0;
            v16 = 0;
            v17 = 0;
            v18 = 0;
            do
            {
              LOBYTE(v7[v0]) = v6[v0 * 2] ^ byte_403000[v0 * 2];
              ++v0;
            }
            while ( v0 < 23 );
            wcsncpy((wchar_t *)v2, v7, (*(_DWORD *)(dword_4031A0 + 8) >> 1) - 1);
          }
          DbgPrint(
            "[NtQueryValueKey] Value Name : %s  Captured !!  Data :  %S\n",
            DestinationString.Buffer,
            dword_4031A0 + 12);
        }
        break;
      }
    }
    RtlFreeAnsiString(&DestinationString);
  }
}
```
it will XOR the previous flag found on the VERIFIER , with a hardcoded array on address ***0x403000*** , that is the corret flag . 
