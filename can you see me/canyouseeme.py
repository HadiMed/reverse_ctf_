import ghidra.program.database.mem.MemoryBlockDB


#Extracting addresses of blocks that contains 0x20

arr=[]


arr.append('30')   
arr.append('86')
arr.append('04')
arr.append('08')
arr.append('98')   
arr.append('86')
arr.append('04')
arr.append('08')
arr.append('0C')   
arr.append('87')
arr.append('04')
arr.append('08')
arr.append('30')   
arr.append('86')
arr.append('04')
arr.append('08')
arr.append('74')   
arr.append('87')
arr.append('04')
arr.append('08')
arr.append('D4')   
arr.append('87')
arr.append('04')
arr.append('08')
arr.append('54')   
arr.append('88')
arr.append('04')
arr.append('08')
arr.append('C0')   
arr.append('88')
arr.append('04')
arr.append('08')
arr.append('98')   
arr.append('86')
arr.append('04')
arr.append('08')
arr.append('30')   
arr.append('89')
arr.append('04')
arr.append('08')
arr.append('54')   
arr.append('88')
arr.append('04')
arr.append('08')
arr.append('9C')   
arr.append('89')
arr.append('04')
arr.append('08')
arr.append('04')   
arr.append('8A')
arr.append('04')
arr.append('08')
arr.append('74')   
arr.append('87')
arr.append('04')
arr.append('08')
arr.append('80')   
arr.append('8A')
arr.append('04')
arr.append('08')
arr.append('E4')   
arr.append('8A')
arr.append('04')
arr.append('08')
arr.append('C0')   
arr.append('88')
arr.append('04')
arr.append('08')
arr.append('4C')   
arr.append('8B')
arr.append('04')
arr.append('08')
arr.append('4C')   
arr.append('8B')
arr.append('04')
arr.append('08')
arr.append('9C')   
arr.append('89')
arr.append('04')
arr.append('08')
arr.append('B0')   
arr.append('8B')
arr.append('04')
arr.append('08')
arr.append('24')   
arr.append('8C')
arr.append('04')
arr.append('08')
adresses = [] 




for x in range(0,len(arr),4) :
    adresses.append(arr[x+3]+arr[x+2]+arr[x+1]+arr[x])
#addresses:

#0x08048630
#0x08048698
#0x0804870C
#0x08048630
#0x08048774
#0x080487D4
#0x08048854
#0x080488C0
#0x08048698
#0x08048930
#0x08048854
#0x0804899C
#0x08048A04
#0x08048774
#0x08048A80
#0x08048AE4
#0x080488C0
#0x08048B4C
#0x08048B4C
#0x0804899C
#0x08048BB0
#0x08048C24





size_of_blocks=[]



# Calculating size of blocks
for x in adresses:
	count = -1 
	result = 1
	_address= int(x,16)
	while result!=0 : # looking for the end of the block
		result= getByte(toAddr(_address))
		count+=1
		_address+=1
	size_of_blocks.append(count)

# Emulating The Program 

seed = 0x30433E9

def random():
    global seed 
    seed = seed + 1 
    return ( seed  * 0x49 ) % 0x16 


counter = 0

flag = [0 for x in range(22)] 

another_counter=0
visited = [0 for x in range(22)]

while(counter < 23) :
    
	ran=random()
	
	if visited[ran]==0 :
        	visited[ran]=1
        	
		flag[ran]=size_of_blocks[counter]
        	
		another_counter+=1
    	counter+=1

print(''.join([chr(x) for x in flag]))

	
	
