## Arm cryped 
the binary provided as soon as it's opened with a disassembler , one can see that it's packed with upx , using the classic known tool to decompress it , we find ourselves with the following binary . 
```
ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, stripped
```
- the binary is dynamicly linked which makes a little challenge to debug it , since it requires some old libraries (libstdc++.so) 
## MAIN function
```C
  uStack72 = 0x2bef6156;
  uStack68 = 0x6cbd209b;
  uStack64 = 0xba206754;
  uStack60 = 0x5e7e20aa;
  uStack56 = 0x3c1a48b1;
  uStack52 = 0x4f327a8a;
  uStack48 = 0x543b;
  uStack46 = 0;
  uStack44 = 0x636e6f6d;
  uStack40 = 0x7365646f;
  uStack36 = 0x65726365;
  uStack32 = 0x74;
  sVar1 = strlen((char *)&uStack72);
  uVar2 = FUN_00008788();
  FUN_000086a0(uVar2,&uStack44,0xd);
  FUN_0000872c(uVar2,&uStack72,&uStack72,sVar1);
  puts("Basic ARM Crypto challenge for Root-Me\nAuthor: koma\n\nFind the flag inside.\n");
  if (iStack28 != __stack_chk_guard) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
- The assumption here is that the flag is from uStack72 to uStack46 and will be decrypted by the 2 calls fo func at addr : 0x000086a0 and 0x0000872c , later turns out  the decryption algorithm is RC4 little modified on the initial conditions . 
## Debugging 
- The idea here is to find a rooted (android phone / emulator) , break after the call to the second function , since it's passing the address of the encrypted flag , it will be changed in the old stack frame (main frame) and , observe the stack for the flag
```asm
      000087dc 39 1c         add       r1,r7,#0x0
      000087de 06 1c         add       r6,r0,#0x0
      000087e0 0d 22         mov       r2,#0xd
      000087e2 ff f7 5d      bl        FUN_000086a0                               undefined FUN_000086a0()
               ff
      000087e6 6a 46         mov       r2,sp
      000087e8 43 46         mov       r3,r8
      000087ea 69 46         mov       r1,sp
      000087ec 30 1c         add       r0,r6,#0x0
      000087ee ff f7 9d      bl        FUN_0000872c                               undefined FUN_0000872c()
               ff
      000087f2 0a 48         ldr       r0,[DAT_0000881c]                          = 000015F8h
      000087f4 78 44         add       r0=>s_Basic_ARM_Crypto_challenge_for_R_00  = "Basic ARM Crypto challeng
      000087f6 ff f7 04      blx       puts                                       int puts(char * __s)
               ef

```
- place a breakpoint in gdb at address 0x87f2 , run the binary , then visualise the stack with x/100s $sp 
