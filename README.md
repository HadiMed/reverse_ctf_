# Write_ups 

1 - "  They are many " , ctf in Cybertalents website link : https://cybertalents.com/challenges/malware/they-are-many
after looking at the disassembly like the description claims  there are a lot of  functions that have the same structure the same size and does the same thing.   using the ghidra API to extract the pre-defined data and emulating the instructions of the function to get the flag .  
 
Structure of the functions :

<br/>

<img src="They are many/ghidra.png"/> 

2 - a x64 elf file  that have a lot of blocks to check each caracter , using the ghidra api to extract all data that is used on the checks . 
2 types of blocks : 
<img src="exe inside elf/ghidra1.png ">
<img src="exe inside elf/ghidra2.png ">
we find that the input is a PE file base64 encoded after decoding it , we find that it basicly does the same thing but the number of blocks is much lesser than the first one , using the ghidra decompiler , i copied all the checks and made it much cleaner .
