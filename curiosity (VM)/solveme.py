from z3 import * 

s = z3.Solver()
Vectors = [z3.BitVec("Vect_{}".format(i), 8) for i in range(28)]

for c in Vectors:
    s.add(z3.And(c >= 0x20,c < 0x7f))


s.add(Vectors[0] + 0xffba == 0)
s.add(Vectors[1]*0x53+0x18+0xe744==0)
s.add(Vectors[2]*0x52+0x4b+0xeae3==0)
s.add(Vectors[3]+0xffb9==0)
s.add(Vectors[4]*0x21+0x2d+0xeff8==0)
s.add(~(Vectors[5]+0x74+0x45)+0x110==0)
s.add(Vectors[6]*0x3c + 0x59 +0xed9b==0)
s.add(Vectors[7]*0x30 + 0x3b +0xedf5 ==0)
s.add(Vectors[8]*0x9 + 0x21 + 0xfd96==0)
s.add(Vectors[9]+0xff92==0)
s.add(Vectors[10]+0xff9f==0)
s.add(~(Vectors[11]+0x6a +0x38)+ 0x1f==0)
s.add(Vectors[12] + 0xff87 ==0)
s.add(Vectors[13] + 0xff8d == 0)
s.add(~(Vectors[14] + 0x38 + 0x4f) + 0xf1 == 0)
s.add(~(Vectors[15]+0x60 + 0x61) + 0x135 == 0)
s.add(~(Vectors[16]+0x5b + 0x5e) + 0x119 == 0)
s.add(~(Vectors[17]+0x48 + 0x32) + 0xe4==0)
s.add(Vectors[18]+0xff8d == 0)
s.add(~(Vectors[19] + 0x28 +0x58 ) +0xe0 ==0)
s.add(~(Vectors[20]+0x50 + 0x74 ) + 0x126 == 0)
s.add(~(Vectors[21] + 0x26 + 0x3e) +0xd2==0)
s.add(~(Vectors[22] + 0x5e +0x6a)+0x12a == 0)
s.add(~(Vectors[23] + 0x6d + 0x2a) + 0x112==0)
s.add(Vectors[24] + 0xff97 ==0)
s.add(Vectors[25] + 0xff92 == 0)
s.add(Vectors[26] + 0xff99 == 0 )
s.add(Vectors[27]*0x27 + 0x40 + 0xecb5==0)

s.check()
m = s.model()
for charr in Vectors:
    print(chr(m[charr].as_long()), end="")
