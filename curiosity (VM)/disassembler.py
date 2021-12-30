def bytes_int(b2,b1) :
    return int(hex(b1).replace("0x","") + hex(b2).replace("0x",""),16)

# bytecodes 
with open("/home/slash/Downloads/challenge/target" , "rb" ) as f :
    VM_data = f.read()

eip = 0


registers = {
    "1" : "register_1",
    "2" : "register_2",
    "3" : "register_3",
    "4" : "register_4"
}


calls_get_char = 0
calls_put_char = 0

reg1 = 0
reg2 = 0
reg3 = 0
reg4 = 0

# opcodes  
instruction = {
    0xFF : "SYSCALL",
    0x1 :"MOV (reg , val)",
    0x2 :"STORE_TO_ADDRESS (address , reg)",
    0x3 :"ADD",
    0x4 :"NOT",
    0x5 :"MULT",
    0x6 :"JMP IF REG1",
    0x7 :"ADD (address , reg)",
}


## Implemeting the logic
while eip < len(VM_data) :
    if VM_data[eip]==0xFF:
        print('\033[93m'+hex(eip)+" :\t" , end="")

        if reg1==2:
            print(instruction[0xFF] + "_EXIT , arg :"+hex(reg2)+"\n")
        elif reg1==1:
            print(instruction[0xFF] + "_PUTCHAR , arg :"+chr(reg2 & 0xff)+"\n")
            calls_put_char+=1
        elif reg1==0:
            print("\n"+instruction[0xFF] + "_GETCHAR, result stored on reg1")
            calls_get_char+=1
    
    elif VM_data[eip] >> 4 == 0x1 :
        print(hex(eip)+" :\t" , end="")
        temp = VM_data[eip] & 3
        eip+=1
        if temp==0 :
            print(instruction[1]+" register_1 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
            reg1 = VM_data[eip]
        if temp==1 :
            print(instruction[1]+" register_2 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
            reg2 = VM_data[eip]
        if temp==2 :
            print(instruction[1]+" register_3 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
            reg3 = VM_data[eip]
        if temp==3 :
            print(instruction[1]+" register_4 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
            reg4 = VM_data[eip]
        eip+=1
        
        

    elif VM_data[eip] >> 4 == 0x2 :
        print(hex(eip)+" :\t" , end="")
        temp = (VM_data[eip] >> 2) & 3
        if temp==0 :
            print(instruction[2]+" [register_1] , "+hex(temp))
        if temp==1 :
            print(instruction[2]+" [register_2] , "+hex(temp))
        if temp==2 :
            print(instruction[2]+" [register_3] , "+hex(temp))
        if temp==3 :
            print(instruction[2]+" [register_4] , "+hex(temp))
        

    elif VM_data[eip] >> 4 == 0x3 :
        print(hex(eip)+" :\t" , end="")

        temp = bytes_int(VM_data[eip],VM_data[eip+1]) & 3
        eip+=1
        if temp==0 :
            reg1 = (reg1 +bytes_int(VM_data[eip],VM_data[eip+1]))
            print(instruction[3]+" register_1 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==1 :
            reg2 = (reg2 +bytes_int(VM_data[eip],VM_data[eip+1]))
            print(instruction[3]+" register_2 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==2 :
            reg3 = (reg3 +bytes_int(VM_data[eip],VM_data[eip+1]))
            print(instruction[3]+" register_3 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==3 :
            reg4 = (reg4 +bytes_int(VM_data[eip],VM_data[eip+1]))
            print(instruction[3]+" register_4 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        eip+=1
        
    
    elif VM_data[eip] >> 4 == 0x4 :
        print(hex(eip)+" :\t" , end="")

        temp = VM_data[eip] & 3
        if temp==0 :
            reg1 =~ reg1 +256
            print(instruction[4]+" register_1")
        if temp==1 :
            reg2 =~ reg2 + 256
            print(instruction[4]+" register_2")
        if temp==2 :
            reg3 =~ reg3 +256
            print(instruction[4]+" register_3")
        if temp==3 :
            reg4 =~ reg4 +256
            print(instruction[4]+" register_4")
        

    elif VM_data[eip] >> 4 == 0x5 :
        print(hex(eip)+" :\t" , end="")

        temp = bytes_int(VM_data[eip],VM_data[eip+1]) & 3 
        eip+=1
        if temp==0 :
            reg1 *= VM_data[eip]
            print(instruction[5]+" register_1 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==1 :
            reg2 *= VM_data[eip]
            print(instruction[5]+" register_2 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==2 :
            reg3 *= VM_data[eip]
            print(instruction[5]+" register_3 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        if temp==3 :
            reg4 *= VM_data[eip]
            print(instruction[5]+" register_4 , "+hex(bytes_int(VM_data[eip],VM_data[eip+1])) )
        eip+=1
        
        

    elif VM_data[eip] >> 4 == 0x6 :
        print(hex(eip)+" :\t" , end="")
        print(instruction[0x6]+" , to reg2")
        print("\n\n")
        
    
    elif VM_data[eip] >> 4 == 0x7 :
        print(hex(eip)+" :\t" , end="")
        temp = (VM_data[eip]  & 3)
        data = (VM_data[eip] >> 2 ) & 3
        if temp==0 :
            print(instruction[7]+" [register_1] , "+registers[str(data+1)])
        if temp==1 :
            print(instruction[7]+" [register_2] , "+registers[str(data+1)])
        if temp==2 :
            print(instruction[7]+" [register_3] , "+registers[str(data+1)])
        if temp==3 :
            print(instruction[7]+" [register_4] , "+registers[str(data+1)])
        

    eip+=1

print("Number of calls to getchar = "+str(calls_get_char))