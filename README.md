# Alienware 
Ransomware encrypts with AES , check writeup for more information
# They are many
1 -</br> ctf in Cybertalents website link : https://cybertalents.com/challenges/malware/they-are-many
after looking at the disassembly like the description claims  there are a lot of  functions that have the same structure the same size and does the same thing.   using the ghidra API to extract the pre-defined data and emulating the instructions of the function to get the flag .  
 
Structure of the functions :

<br/>

<img src="They are many/ghidra.png"/> 

# Exe inside elf
2 <br/> a x64 elf file<a href="Exe inside elf/executable"> Executable here </a>  that have a lot of blocks to check each caracter , using the ghidra api to extract all data that is used on the checks . 
structure of blocks : 
<br/>
<img src="Exe inside elf/ghidra1.png ">

we find that the input is a PE file base64 encoded ,after decoding it  we find that it basicly does the same thing but the number of blocks is much lesser than the first one , using the ghidra decompiler , i copied all the checks and made it much cleaner .
# Can you see me 
3 -link : https://cybertalents.com/challenges/malware/can-you-see-me </b>

# KILLJOY

4 - challenge on the mini ctf in cyer talents week 4 ,  it uses TEA algorithm to encrypt the input with a hardcoded key and compare it to a hardcoded password , that password is the flag . 

# No Breakpoint

5 - the executable uses an anti debugging technique , that checks if the code was modified so if we use software breakpoints , the hash algorithm will detect it and the result will be false 

# Rokai 

6 -  Challenges at cyebertalents , link : https://hubchallenges.s3-eu-west-1.amazonaws.com/Reverse/Rokai492084659892759472878.apk , look <a href="Rokai/">writeup</a> .
