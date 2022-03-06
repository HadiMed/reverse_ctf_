#include "pch.h"

#include <stdio.h>

void FLY()
;

BYTE patch[] = { 0x90,0x90,0x90,0x90 }
    ;
BYTE OLD_VALUES[] = { 0xC6, 0x43 , 0x20 ,0x00 }
;
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        FLY();
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

void FLY() 
{
    AllocConsole()
        ;
    FILE* f
        ;
    freopen_s(&f, "CONOUT$", "w", stdout)
        ;


    /*
    BEFORE PATCH : 
        GameAssembly.dll+8326DD - C6 43 20 00  mov byte ptr [rbx+20],00
    */

    
    BYTE* TARGET_TO_PATCH = (BYTE*)((uintptr_t)GetModuleHandleA("GameAssembly.dll") + 0x8326DD);

 
    printf("[+] Memory Address to Patch @ 0x%llx\n", TARGET_TO_PATCH)
        ;
    DWORD newprotect =0
        ;
    DWORD oldProtect = 0
        ;
    BOOL HACK_ENABLED = 0
        ;

blah :
    while(1)
    {
        if (GetAsyncKeyState(VK_SHIFT) && GetAsyncKeyState(VK_TAB)) {

            HACK_ENABLED = TRUE
                ; 
            puts("[+] FLY HACK ENABLED !\n")
                ;
            break;
        }
    }

    if (!VirtualProtect(TARGET_TO_PATCH, 4, PAGE_EXECUTE_READWRITE, &oldProtect))
    {
        puts("Couldnt change memory protection , exiting")
            ;
        
        return
            ;
    }
    /*
    AFTER PATCH :
    
        GameAssembly.dll+8326DD - 90 90 90 90  nop nop nop nop
    */

    CopyMemory(TARGET_TO_PATCH,patch,4); 

    if (!VirtualProtect(TARGET_TO_PATCH, 4, PAGE_EXECUTE_READ, &oldProtect))
    {
        puts("Couldnt change memory protection , exiting")
            ;
        return
            ;
    }
    while (1)
    {
        if (GetAsyncKeyState(VK_SHIFT) && GetAsyncKeyState(VK_TAB)) {

            HACK_ENABLED = FALSE
                ;
            puts("[+] FLY HACK DISABLED !\n")
                ;
            break
                ;
            if (!VirtualProtect(TARGET_TO_PATCH, 4, PAGE_EXECUTE_READWRITE, &oldProtect))
            {
                puts("Couldnt change memory protection , exiting")
                    ;

                return
                    ;
            }
            /*
            AFTER PATCH :

                GameAssembly.dll+8326DD - 90 90 90 90  nop nop nop nop
            */

            CopyMemory(TARGET_TO_PATCH, OLD_VALUES, 4);

            if (!VirtualProtect(TARGET_TO_PATCH, 4, PAGE_EXECUTE_READ, &oldProtect))
            {
                puts("Couldnt change memory protection , exiting")
                    ;
                return
                    ;
            }
        }
    }
}




