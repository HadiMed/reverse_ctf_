## Writeup

***Since Almost Everything can be solved by flying , Coding a Fly Hack seems the best way to go***

- Function Responsible For Jumping : 

![movementJUMP](https://user-images.githubusercontent.com/57273771/156937256-aab947b0-bbe3-4a83-958d-14383fc52d7e.PNG)

- This is the instruction that change the Z coordinate to ZERO , it grounds the ball 

![patch](https://user-images.githubusercontent.com/57273771/156937280-5798e906-3cbb-441a-8010-666a30303911.PNG)

- Patching this instructions with NOPs will have the effect of not assigning 0 to the Z coordinate which mean if if keep pressing space ,
i'll keep jumping incrementing Z which mean I keep Jumping <br/>

- Use any DLL injector to inject the FLY MODE  , For Me I used this one  https://github.com/HadiMed/Dll_injector

# Usage :
  ```Inject.exe Ctf.exe Full_path_of_the_DLL_FROM_C_DRIVE```
