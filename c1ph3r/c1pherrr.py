# Exctrating exponents and primes numbers 
with open("C:\\Users\\Slashroot\\Desktop\\C1ph3r.exe","rb") as f :
    filedata = f.read()
    data_factorization = list(filedata[0xA560:0x2B5F0])
    data_section_primes_bytes =   list(filedata[0x8A37:0xA560])

data_section_primes_bytes[108] = 1
data_section_primes_double_bytes = ['' for x in range(len(data_section_primes_bytes)) ] 
y=0


for x in range(len(data_section_primes_bytes)//2 )  : 
    byte1 =  hex(data_section_primes_bytes[2*x]).replace("0x","") 
    byte2 =  hex(data_section_primes_bytes[2*x+1]).replace("0x","")
    data_section_primes_double_bytes[2*y] = int('0'* (2-len(byte1))+byte1 +  '0'*(2- len(byte2)) + byte2 ,16)
    data_section_primes_double_bytes[2*y+1]=0
    y+=1



flag = ""
eax = 0 



# Looping on flag , since we work with 2 caracters at once we need to loop on the half 
for _ in range(0x10):
    
    prime_factorization_result =  1
    for x in range(0xd94): 
        
        prime_factorization_result *=data_section_primes_double_bytes[x] ** data_factorization[eax+x]
    garbage= hex(prime_factorization_result).replace("0x","")
    flag+=chr(int(garbage[:2],16)) + chr(int(garbage[2:],16))

    eax+=0x1B28
print(flag)  

               
        
