
import base64

func_body = getGlobalFunctions('check')[0].getBody()


listing = currentProgram.getListing()
opiter = listing.getInstructions(func_body, True)
i= 0 

XOR1=[]
XOR2=[]

count = False
i=0
while opiter.hasNext() : 
	# extracting data from all function disassembly 
        # Taking into account that some blocks doesnt have the same general structure 	
	op=opiter.next()
	
	if str(op)[:26] == "MOV dword ptr [RBP + -0x8]": 
		XOR1.append(str(op)[-2:].replace('x',''))
		count = True 
	if count : 
		i+=1 
		
		
	if str(op)[:3] == "XOR": 
		
		XOR2.append(str(op)[-2:].replace('x',''))	
		count = False 
		i=0 
		
	if i> 8 :
		XOR2.append(' ')
		count = False 
		i=0
	
		


	

	
output = "" 
for i in range(len(XOR1)) : 
	if XOR2[i] == " " : # the blocks without XOR stays the same 
		output += chr(int(XOR1[i],16) )
		continue
	output += chr(int(XOR1[i],16) ^ int(XOR2[i],16))

with open("input","wb") as f :
	f.write(base64.b64decode(output)) 
