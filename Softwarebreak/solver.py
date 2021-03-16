rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))


data ="b804000000bb01000000b9a1910408ba26000000cd80b80300000031dbb988910408ba33000000cd8031c9b880800408bb23810408e85b00000089cab919000000b855910408bb88910408d1ca8a4408ff8a5c0bff30d830d0751b4975e3b804000000bb01000000b924910408ba26000000cd80eb16b804000000bb01000000b94a910408ba0b000000cd80b80100000031dbcd8029c331c90208c1c103404b75f7c3"
ebx_eax = []
for x in range(0,len(data)-1,2) :
    ebx_eax.append(int(data[x]+data[x+1],16))

ebx = 0x123 - 0x80

al = 0
cl= 0
ecx = 0x00000000
while ebx != 0  :
    cl = (cl + ebx_eax[al]) % 256
    print("cl="+hex(cl),end=" ")
    hexecx=('%08X' % ecx )[:-2] + ('%02X' % cl)
    
    print("ecx="+hexecx,end=" ")
    ecx = rol(int(hexecx,16) , 3 , 32)
    cl = int(hex(ecx).replace("0x","")[-2:],16)
    print("cl="+hex(cl),end=" ")
    print("ecx="+hex(ecx))


    #cl=int(hex(ecx).replace('0x','')[-2:],16)
    al+=1
    ebx-=1
print("Hash of instructions : "+hex(ecx))
edx= ecx

ecx = 25
data = "1ecd2ad53487fc7864359decde15ac9799af96da79264f32e0"
Anotherdata = "" # empty ebx my data 
eax = []
for x in range(0,len(data)-1,2) :
    eax.append(int(data[x]+data[x+1],16))

flag=""
while ecx != 0 :
    edx=ror(edx,1 ,32)

    flag=chr(int(hex(edx)[-2:],16)^eax[ecx-1])+flag
    ecx -=1

print("Flag = "+flag)
