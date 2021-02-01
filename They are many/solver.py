 


Functionlist = [] 
i=0
func = getFirstFunction()
while func is not None:
	if i>=13 : # passing the first libc and predefined 13 functions 
    		Functionlist.append(func.getName())
    	func = getFunctionAfter(func)	
	i+=1

Functionlist = Functionlist[:-9] # passing 9 functions at the end other predefined functions
for func in Functionlist : 
	
	func_body = getGlobalFunctions(func)[0].getBody()
    	listing = currentProgram.getListing()
    	opiter = listing.getInstructions(func_body, True) # Disassembly instructions of the function
	i=0
	local40 = [] 
	local_30=[]
	while opiter.hasNext()  : # looping throught the instructions 
		op=opiter.next() #
		raw_pcode = op.getPcode()
		if i >= 4 and i <12 : # extraction the local30 predefined array 
			local_30.append("{}".format(op)[28:])
        	if i >=12 and i<=15  : # extracting the predefined local40 array 
			local40.append("{}".format(op)[28:])
		if i==15 : 
			break # instuction 15 is the last one we need 
				
			  
			
		i+=1	
	if local40[-1]!='EAX': # There is some functions that we dont need on the middle we leave them out
		#Basic operations for making the bytes ready for the XOR operation 
		local40 = [x.replace("0x","") for x in local40]
	
		local30=["0"+x if len(x)==7 else x  for x in [x.replace("0x","") for x in local_30] ]
	
		local_30 = [] 
		for x in local30 :
			for y in range(len(x)-1,-1,-2) : 
				local_30.append(x[y-1]+x[y]) 
	
		result =[]
                # Emulating the function 
		for x in range(len(local_30)) : 
			result.append(  int(local40[x & 3 ],16) ^ int(local_30[x],16)) 
		output = '' 
		for x in result : 

			output += chr(x)
		if output[:2] == 'fl' : # Finding the function that will give the flag  
			print "Found: "+output
                        break 
		


	
