#Decipher TEA algorithm with predefined key 


def decipher(v, k):
    y=v[0]
    z=v[1]
    sum=0xC6EF3720
    delta=0x9E3779B9
    n=32
    w=[0,0]
   

    while(n>0):
        z -= (y << 4 ^ y >> 5) + y ^ sum + k[sum>>11 & 3]
        z &= 4294967295
        sum -= delta
        y -= (z << 4 ^ z >> 5) + z ^ sum + k[sum&3]
        y &= 4294967295
        n -= 1

    w[0]=hex(y); w[1]=hex(z)
    return w

key = [ 0x34561234,0x111F3423,0x1333337,0x34D57910]

local_2d0=[0 for x in range(8)]
local_2d0[0] = 0xd6f74320;
local_2d0[1] = 0x636a7b0a;
local_2d0[2] = 0xeec58e45;
local_2d0[3] = 0x5f1e3af5;
local_2d0[4] = 0x14d72088;
local_2d0[5] = 0x819bf516;
local_2d0[6] = 0x10a4d83a;
local_2d0[7] = 0x2c1001e7;
i=0
output=[]
while i<8:
        output.append(decipher(local_2d0[i:i+2],key))
        i=i+2

flag=""
for y in output:
        for x in y : 
                tmp = x.replace("0x","")
                flag+=chr(int(tmp[:2],16))+chr(int(tmp[2:4],16))+chr(int(tmp[4:6],16))+chr(int(tmp[6:],16))

print(flag)
