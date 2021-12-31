## Writeup
- The methodology on analyzing a VM varies , depending on the VM but mainly it relies on understanding what the opcodes do , and find a way to emulate or monitor the behaviour of the VM using  DBI's for example , For me I tried to make a disassembler and an emulator to have an idea about the algorithm  .
- Static analysis shows this VM uses 4 registers , and 8 operations (mov , add , not , syscall , jmp cond , mult , ,mov to add , add to add) those ops are well defined on the disasemlby to make the operations more understandable
- disassembly :

```
0x0 :	MOV (reg , val) register_1 , 0x1
0x3 :	MOV (reg , val) register_2 , 0xcc
0x6 :	JMP IF REG1 , to reg2



0x7 :	MOV (reg , val) register_1 , 0x1
0xa :	MOV (reg , val) register_2 , 0xde
0xd :	ADD register_2 , 0x69
0x10 :	SYSCALL_PUTCHAR , arg :G

0x11 :	MOV (reg , val) register_2 , 0x2f
0x14 :	ADD register_2 , 0x40
0x17 :	SYSCALL_PUTCHAR , arg :o

0x18 :	MOV (reg , val) register_2 , 0x43
0x1b :	ADD register_2 , 0x2c
0x1e :	SYSCALL_PUTCHAR , arg :o

0x1f :	MOV (reg , val) register_2 , 0x9b
0x22 :	NOT register_2
0x23 :	SYSCALL_PUTCHAR , arg :d

0x24 :	MOV (reg , val) register_2 , 0xdf
0x27 :	NOT register_2
0x28 :	SYSCALL_PUTCHAR , arg : 

0x29 :	MOV (reg , val) register_2 , 0x8f
0x2c :	NOT register_2
0x2d :	SYSCALL_PUTCHAR , arg :p

0x2e :	MOV (reg , val) register_2 , 0xfe
0x31 :	ADD register_2 , 0x63
0x34 :	SYSCALL_PUTCHAR , arg :a

0x35 :	MOV (reg , val) register_2 , 0x4f
0x38 :	ADD register_2 , 0x24
0x3b :	SYSCALL_PUTCHAR , arg :s

0x3c :	MOV (reg , val) register_2 , 0x3b
0x3f :	ADD register_2 , 0x38
0x42 :	SYSCALL_PUTCHAR , arg :s

0x43 :	MOV (reg , val) register_2 , 0x47
0x46 :	ADD register_2 , 0x30
0x49 :	SYSCALL_PUTCHAR , arg :w

0x4a :	MOV (reg , val) register_2 , 0x4e
0x4d :	ADD register_2 , 0x21
0x50 :	SYSCALL_PUTCHAR , arg :o

0x51 :	MOV (reg , val) register_2 , 0x8d
0x54 :	NOT register_2
0x55 :	SYSCALL_PUTCHAR , arg :r

0x56 :	MOV (reg , val) register_2 , 0x9b
0x59 :	NOT register_2
0x5a :	SYSCALL_PUTCHAR , arg :d

0x5b :	MOV (reg , val) register_2 , 0xf5
0x5e :	NOT register_2
0x5f :	SYSCALL_PUTCHAR , arg :


0x60 :	MOV (reg , val) register_1 , 0x2
0x63 :	MOV (reg , val) register_2 , 0x0
0x66 :	SYSCALL_EXIT , arg :0x0

0x67 :	MOV (reg , val) register_1 , 0x1
0x6a :	MOV (reg , val) register_2 , 0x19
0x6d :	ADD register_2 , 0x3e
0x70 :	SYSCALL_PUTCHAR , arg :W

0x71 :	MOV (reg , val) register_2 , 0x8d
0x74 :	NOT register_2
0x75 :	SYSCALL_PUTCHAR , arg :r

0x76 :	MOV (reg , val) register_2 , 0x5a
0x79 :	ADD register_2 , 0x15
0x7c :	SYSCALL_PUTCHAR , arg :o

0x7d :	MOV (reg , val) register_2 , 0x91
0x80 :	NOT register_2
0x81 :	SYSCALL_PUTCHAR , arg :n

0x82 :	MOV (reg , val) register_2 , 0x18
0x85 :	ADD register_2 , 0x4f
0x88 :	SYSCALL_PUTCHAR , arg :g

0x89 :	MOV (reg , val) register_2 , 0xdf
0x8c :	NOT register_2
0x8d :	SYSCALL_PUTCHAR , arg : 

0x8e :	MOV (reg , val) register_2 , 0x8f
0x91 :	NOT register_2
0x92 :	SYSCALL_PUTCHAR , arg :p

0x93 :	MOV (reg , val) register_2 , 0xf9
0x96 :	ADD register_2 , 0x68
0x99 :	SYSCALL_PUTCHAR , arg :a

0x9a :	MOV (reg , val) register_2 , 0x5d
0x9d :	ADD register_2 , 0x16
0xa0 :	SYSCALL_PUTCHAR , arg :s

0xa1 :	MOV (reg , val) register_2 , 0x21
0xa4 :	ADD register_2 , 0x52
0xa7 :	SYSCALL_PUTCHAR , arg :s

0xa8 :	MOV (reg , val) register_2 , 0x65
0xab :	ADD register_2 , 0x12
0xae :	SYSCALL_PUTCHAR , arg :w

0xaf :	MOV (reg , val) register_2 , 0xfc
0xb2 :	ADD register_2 , 0x73
0xb5 :	SYSCALL_PUTCHAR , arg :o

0xb6 :	MOV (reg , val) register_2 , 0x8d
0xb9 :	NOT register_2
0xba :	SYSCALL_PUTCHAR , arg :r

0xbb :	MOV (reg , val) register_2 , 0x9b
0xbe :	NOT register_2
0xbf :	SYSCALL_PUTCHAR , arg :d

0xc0 :	MOV (reg , val) register_2 , 0xf5
0xc3 :	NOT register_2
0xc4 :	SYSCALL_PUTCHAR , arg :


0xc5 :	MOV (reg , val) register_1 , 0x2
0xc8 :	MOV (reg , val) register_2 , 0x1
0xcb :	SYSCALL_EXIT , arg :0x1

0xcc :	MOV (reg , val) register_1 , 0x1
0xcf :	MOV (reg , val) register_2 , 0x43
0xd2 :	ADD register_2 , 0x2
0xd5 :	SYSCALL_PUTCHAR , arg :E

0xd6 :	MOV (reg , val) register_2 , 0x91
0xd9 :	NOT register_2
0xda :	SYSCALL_PUTCHAR , arg :n

0xdb :	MOV (reg , val) register_2 , 0x8b
0xde :	NOT register_2
0xdf :	SYSCALL_PUTCHAR , arg :t

0xe0 :	MOV (reg , val) register_2 , 0x5f
0xe3 :	ADD register_2 , 0x6
0xe6 :	SYSCALL_PUTCHAR , arg :e

0xe7 :	MOV (reg , val) register_2 , 0x8d
0xea :	NOT register_2
0xeb :	SYSCALL_PUTCHAR , arg :r

0xec :	MOV (reg , val) register_2 , 0xdf
0xef :	NOT register_2
0xf0 :	SYSCALL_PUTCHAR , arg : 

0xf1 :	MOV (reg , val) register_2 , 0x8f
0xf4 :	NOT register_2
0xf5 :	SYSCALL_PUTCHAR , arg :p

0xf6 :	MOV (reg , val) register_2 , 0x14
0xf9 :	ADD register_2 , 0x4d
0xfc :	SYSCALL_PUTCHAR , arg :a

0xfd :	MOV (reg , val) register_2 , 0x2d
0x100 :	ADD register_2 , 0x46
0x103 :	SYSCALL_PUTCHAR , arg :s

0x104 :	MOV (reg , val) register_2 , 0x20
0x107 :	ADD register_2 , 0x53
0x10a :	SYSCALL_PUTCHAR , arg :s

0x10b :	MOV (reg , val) register_2 , 0x46
0x10e :	ADD register_2 , 0x31
0x111 :	SYSCALL_PUTCHAR , arg :w

0x112 :	MOV (reg , val) register_2 , 0x4f
0x115 :	ADD register_2 , 0x20
0x118 :	SYSCALL_PUTCHAR , arg :o

0x119 :	MOV (reg , val) register_2 , 0x8d
0x11c :	NOT register_2
0x11d :	SYSCALL_PUTCHAR , arg :r

0x11e :	MOV (reg , val) register_2 , 0x9b
0x121 :	NOT register_2
0x122 :	SYSCALL_PUTCHAR , arg :d

0x123 :	MOV (reg , val) register_2 , 0xc5
0x126 :	NOT register_2
0x127 :	SYSCALL_PUTCHAR , arg ::

0x128 :	MOV (reg , val) register_2 , 0xdf
0x12b :	NOT register_2
0x12c :	SYSCALL_PUTCHAR , arg : 

0x12d :	MOV (reg , val) register_4 , 0x0
0x130 :	MOV (reg , val) register_1 , 0x0
0x133 :	
SYSCALL_GETCHAR, result stored on reg1
0x134 :	MOV (reg , val) register_3 , 0xffba
0x137 :	ADD (address , reg) [register_1] , register_3
0x138 :	ADD (address , reg) [register_4] , register_1
0x139 :	MOV (reg , val) register_1 , 0x0
0x13c :	
SYSCALL_GETCHAR, result stored on reg1
0x13d :	MULT register_1 , 0x53
0x140 :	MOV (reg , val) register_3 , 0x18
0x143 :	ADD (address , reg) [register_1] , register_3
0x144 :	ADD register_1 , 0xe744
0x147 :	ADD (address , reg) [register_4] , register_1
0x148 :	MOV (reg , val) register_1 , 0x0
0x14b :	
SYSCALL_GETCHAR, result stored on reg1
0x14c :	MULT register_1 , 0x52
0x14f :	MOV (reg , val) register_3 , 0x4b
0x152 :	ADD (address , reg) [register_1] , register_3
0x153 :	ADD register_1 , 0xeae3
0x156 :	ADD (address , reg) [register_4] , register_1
0x157 :	MOV (reg , val) register_1 , 0x0
0x15a :	
SYSCALL_GETCHAR, result stored on reg1
0x15b :	MOV (reg , val) register_3 , 0xffb9
0x15e :	ADD (address , reg) [register_1] , register_3
0x15f :	ADD (address , reg) [register_4] , register_1
0x160 :	MOV (reg , val) register_1 , 0x0
0x163 :	
SYSCALL_GETCHAR, result stored on reg1
0x164 :	MULT register_1 , 0x21
0x167 :	MOV (reg , val) register_3 , 0x2d
0x16a :	ADD (address , reg) [register_1] , register_3
0x16b :	ADD register_1 , 0xeff8
0x16e :	ADD (address , reg) [register_4] , register_1
0x16f :	MOV (reg , val) register_1 , 0x0
0x172 :	
SYSCALL_GETCHAR, result stored on reg1
0x173 :	MOV (reg , val) register_3 , 0x74
0x176 :	ADD register_3 , 0x45
0x179 :	ADD (address , reg) [register_1] , register_3
0x17a :	NOT register_1
0x17b :	ADD register_1 , 0x110
0x17e :	ADD (address , reg) [register_4] , register_1
0x17f :	MOV (reg , val) register_1 , 0x0
0x182 :	
SYSCALL_GETCHAR, result stored on reg1
0x183 :	MULT register_1 , 0x3c
0x186 :	MOV (reg , val) register_3 , 0x59
0x189 :	ADD (address , reg) [register_1] , register_3
0x18a :	ADD register_1 , 0xed9b
0x18d :	ADD (address , reg) [register_4] , register_1
0x18e :	MOV (reg , val) register_1 , 0x0
0x191 :	
SYSCALL_GETCHAR, result stored on reg1
0x192 :	MULT register_1 , 0x30
0x195 :	MOV (reg , val) register_3 , 0x3b
0x198 :	ADD (address , reg) [register_1] , register_3
0x199 :	ADD register_1 , 0xedf5
0x19c :	ADD (address , reg) [register_4] , register_1
0x19d :	MOV (reg , val) register_1 , 0x0
0x1a0 :	
SYSCALL_GETCHAR, result stored on reg1
0x1a1 :	MULT register_1 , 0x9
0x1a4 :	MOV (reg , val) register_3 , 0x21
0x1a7 :	ADD (address , reg) [register_1] , register_3
0x1a8 :	ADD register_1 , 0xfd96
0x1ab :	ADD (address , reg) [register_4] , register_1
0x1ac :	MOV (reg , val) register_1 , 0x0
0x1af :	
SYSCALL_GETCHAR, result stored on reg1
0x1b0 :	MOV (reg , val) register_3 , 0xff92
0x1b3 :	ADD (address , reg) [register_1] , register_3
0x1b4 :	ADD (address , reg) [register_4] , register_1
0x1b5 :	MOV (reg , val) register_1 , 0x0
0x1b8 :	
SYSCALL_GETCHAR, result stored on reg1
0x1b9 :	MOV (reg , val) register_3 , 0xff9f
0x1bc :	ADD (address , reg) [register_1] , register_3
0x1bd :	ADD (address , reg) [register_4] , register_1
0x1be :	MOV (reg , val) register_1 , 0x0
0x1c1 :	
SYSCALL_GETCHAR, result stored on reg1
0x1c2 :	MOV (reg , val) register_3 , 0x6a
0x1c5 :	ADD register_3 , 0x38
0x1c8 :	ADD (address , reg) [register_1] , register_3
0x1c9 :	NOT register_1
0x1ca :	ADD register_1 , 0x1f
0x1cd :	ADD (address , reg) [register_4] , register_1
0x1ce :	MOV (reg , val) register_1 , 0x0
0x1d1 :	
SYSCALL_GETCHAR, result stored on reg1
0x1d2 :	MOV (reg , val) register_3 , 0xff87
0x1d5 :	ADD (address , reg) [register_1] , register_3
0x1d6 :	ADD (address , reg) [register_4] , register_1
0x1d7 :	MOV (reg , val) register_1 , 0x0
0x1da :	
SYSCALL_GETCHAR, result stored on reg1
0x1db :	MOV (reg , val) register_3 , 0xff8d
0x1de :	ADD (address , reg) [register_1] , register_3
0x1df :	ADD (address , reg) [register_4] , register_1
0x1e0 :	MOV (reg , val) register_1 , 0x0
0x1e3 :	
SYSCALL_GETCHAR, result stored on reg1
0x1e4 :	MOV (reg , val) register_3 , 0x38
0x1e7 :	ADD register_3 , 0x4f
0x1ea :	ADD (address , reg) [register_1] , register_3
0x1eb :	NOT register_1
0x1ec :	ADD register_1 , 0xf1
0x1ef :	ADD (address , reg) [register_4] , register_1
0x1f0 :	MOV (reg , val) register_1 , 0x0
0x1f3 :	
SYSCALL_GETCHAR, result stored on reg1
0x1f4 :	MOV (reg , val) register_3 , 0x60
0x1f7 :	ADD register_3 , 0x61
0x1fa :	ADD (address , reg) [register_1] , register_3
0x1fb :	NOT register_1
0x1fc :	ADD register_1 , 0x135
0x1ff :	ADD (address , reg) [register_4] , register_1
0x200 :	MOV (reg , val) register_1 , 0x0
0x203 :	
SYSCALL_GETCHAR, result stored on reg1
0x204 :	MOV (reg , val) register_3 , 0x5b
0x207 :	ADD register_3 , 0x5e
0x20a :	ADD (address , reg) [register_1] , register_3
0x20b :	NOT register_1
0x20c :	ADD register_1 , 0x119
0x20f :	ADD (address , reg) [register_4] , register_1
0x210 :	MOV (reg , val) register_1 , 0x0
0x213 :	
SYSCALL_GETCHAR, result stored on reg1
0x214 :	MOV (reg , val) register_3 , 0x48
0x217 :	ADD register_3 , 0x32
0x21a :	ADD (address , reg) [register_1] , register_3
0x21b :	NOT register_1
0x21c :	ADD register_1 , 0xe4
0x21f :	ADD (address , reg) [register_4] , register_1
0x220 :	MOV (reg , val) register_1 , 0x0
0x223 :	
SYSCALL_GETCHAR, result stored on reg1
0x224 :	MOV (reg , val) register_3 , 0xff8d
0x227 :	ADD (address , reg) [register_1] , register_3
0x228 :	ADD (address , reg) [register_4] , register_1
0x229 :	MOV (reg , val) register_1 , 0x0
0x22c :	
SYSCALL_GETCHAR, result stored on reg1
0x22d :	MOV (reg , val) register_3 , 0x28
0x230 :	ADD register_3 , 0x58
0x233 :	ADD (address , reg) [register_1] , register_3
0x234 :	NOT register_1
0x235 :	ADD register_1 , 0xe0
0x238 :	ADD (address , reg) [register_4] , register_1
0x239 :	MOV (reg , val) register_1 , 0x0
0x23c :	
SYSCALL_GETCHAR, result stored on reg1
0x23d :	MOV (reg , val) register_3 , 0x50
0x240 :	ADD register_3 , 0x74
0x243 :	ADD (address , reg) [register_1] , register_3
0x244 :	NOT register_1
0x245 :	ADD register_1 , 0x126
0x248 :	ADD (address , reg) [register_4] , register_1
0x249 :	MOV (reg , val) register_1 , 0x0
0x24c :	
SYSCALL_GETCHAR, result stored on reg1
0x24d :	MOV (reg , val) register_3 , 0x26
0x250 :	ADD register_3 , 0x3e
0x253 :	ADD (address , reg) [register_1] , register_3
0x254 :	NOT register_1
0x255 :	ADD register_1 , 0xd2
0x258 :	ADD (address , reg) [register_4] , register_1
0x259 :	MOV (reg , val) register_1 , 0x0
0x25c :	
SYSCALL_GETCHAR, result stored on reg1
0x25d :	MOV (reg , val) register_3 , 0x5e
0x260 :	ADD register_3 , 0x6a
0x263 :	ADD (address , reg) [register_1] , register_3
0x264 :	NOT register_1
0x265 :	ADD register_1 , 0x12a
0x268 :	ADD (address , reg) [register_4] , register_1
0x269 :	MOV (reg , val) register_1 , 0x0
0x26c :	
SYSCALL_GETCHAR, result stored on reg1
0x26d :	MOV (reg , val) register_3 , 0x6d
0x270 :	ADD register_3 , 0x2a
0x273 :	ADD (address , reg) [register_1] , register_3
0x274 :	NOT register_1
0x275 :	ADD register_1 , 0x112
0x278 :	ADD (address , reg) [register_4] , register_1
0x279 :	MOV (reg , val) register_1 , 0x0
0x27c :	
SYSCALL_GETCHAR, result stored on reg1
0x27d :	MOV (reg , val) register_3 , 0xff97
0x280 :	ADD (address , reg) [register_1] , register_3
0x281 :	ADD (address , reg) [register_4] , register_1
0x282 :	MOV (reg , val) register_1 , 0x0
0x285 :	
SYSCALL_GETCHAR, result stored on reg1
0x286 :	MOV (reg , val) register_3 , 0xff92
0x289 :	ADD (address , reg) [register_1] , register_3
0x28a :	ADD (address , reg) [register_4] , register_1
0x28b :	MOV (reg , val) register_1 , 0x0
0x28e :	
SYSCALL_GETCHAR, result stored on reg1
0x28f :	MOV (reg , val) register_3 , 0xff99
0x292 :	ADD (address , reg) [register_1] , register_3
0x293 :	ADD (address , reg) [register_4] , register_1
0x294 :	MOV (reg , val) register_1 , 0x0
0x297 :	
SYSCALL_GETCHAR, result stored on reg1
0x298 :	MULT register_1 , 0x27
0x29b :	MOV (reg , val) register_3 , 0x40
0x29e :	ADD (address , reg) [register_1] , register_3
0x29f :	ADD register_1 , 0xecb5
0x2a2 :	ADD (address , reg) [register_4] , register_1
0x2a3 :	STORE_TO_ADDRESS (address , reg) [register_4] , 0x3
0x2a4 :	MOV (reg , val) register_2 , 0x67
0x2a7 :	JMP IF REG1 , to reg2



0x2a8 :	MOV (reg , val) register_1 , 0x1
0x2ab :	MOV (reg , val) register_2 , 0x7
0x2ae :	JMP IF REG1 , to reg2

```
- About instructions , JMP instruction will jump to whatever is in reg2 in condition that reg1 is not null , 
- control flow : The program will first jump to address 0xCC , print "Enter Password : " , do some operations on each character of the input I assumed that the result should be 0 because on the jump before the last one , register1 should be 0 which holds the results of the operations , if it's not zero the control flow will be transfered to the part that prints wrong pass , anyway I used Z3 to solve the system conditions .
### END
