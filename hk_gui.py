from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from pymem import Pymem
from pymem.ptypes import RemotePointer
from pymem import *
from pymem.process import *
import sv_ttk

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset

pm = Pymem("hollow_knight.exe")
gameModule = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll

def none():
    pass

def loadProcess():
    gameModule = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
    tkinter.messagebox.showinfo("Success", "hollow_knight.exe loaded\nAddress: " + str(gameModule))
    geo = pm.read_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x1C4]))
    geoEntry['state'] = 'normal'
    geoEntry.insert(0, geo)
    saveBtn['state'] = 'normal'
    infJumpCheck['state'] = 'normal'
    infSoulCheck['state'] = 'normal'
    invincibilityCheck['state'] = 'normal'
    abilityCheck['state'] = 'normal'
    mapCheck['state'] = 'normal'
    stagCheck['state'] = 'normal'
    allCharmsCheck['state'] = 'normal'

def infJump():
    infJumpStatusCheck = infJumpStatus.get()
    print(f"Inf: {infJumpStatusCheck}")
    if infJumpStatusCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF4]), 1)
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF4]), 0)
    
def infSoul():
    infSoulStausCheck = infSoulStatus.get()
    print(f"Insl: {infSoulStausCheck}")
    if infSoulStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x1CC]), 99999)
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x1CC]), 0)

def invincibility():
    invincibility = pm.read_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF3]))
    print(invincibility)

    invincibilityStausCheck = invincibilityStatus.get()
    print(f"Inv: {invincibilityStausCheck}")
    if invincibilityStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF3]), 1)
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF3]), 0)


def unlockAllAbilites():
    abilityStausCheck = abilityStatus.get()
    if abilityStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x284]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x258]), 10)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x285]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x286]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x287]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x289]), 1)
        
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x284]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x258]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x285]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x286]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x287]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x289]), 0)
        
def allCharms():
    allCharmsStausCheck = allCharmsStatus.get()
    if allCharmsStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4DB]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4E2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4EA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4F2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4FA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x502]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x50A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x512]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x51A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x522]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x52A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x532]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x53A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x542]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x54A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x552]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x55A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x562]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x56A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x572]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x57A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x582]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x58A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x592]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x59A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5A2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5AA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5B2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5BA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5C2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5CA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5D2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5DA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5E2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5EA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5F2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5FA]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x602]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x60A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x612]), 1)

    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4DB]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4E2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4EA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4F2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4FA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x502]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x50A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x512]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x51A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x522]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x52A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x532]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x53A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x542]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x54A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x552]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x55A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x562]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x56A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x572]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x57A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x582]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x58A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x592]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x59A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5A2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5AA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5B2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5BA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5C2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5CA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5D2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5DA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5E2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5EA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5F2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x5FA]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x602]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x60A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x612]), 0)

def unlockAllMaps():
    mapStausCheck = mapStatus.get()
    if mapStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC10]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC11]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC12]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC13]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC14]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC15]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC16]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC17]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC18]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC19]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1B]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1C]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1D]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1E]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1F]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC20]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC21]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC22]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC23]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC24]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC25]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC26]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC27]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC28]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC29]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2A]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2B]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2C]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2D]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2E]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2F]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC30]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC31]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC34]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC38]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC3C]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC40]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x28C]), 1)
        
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC10]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC11]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC12]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC13]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC14]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC15]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC16]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC17]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC18]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC19]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1B]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1C]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1D]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1E]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC1F]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC20]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC21]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC22]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC23]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC24]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC25]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC26]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC27]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC28]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC29]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2A]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2B]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2C]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2D]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2E]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC2F]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC30]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC31]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC34]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC38]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC3C]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC40]), 0)

def unlockAllStagsTrams():
    stagStausCheck = stagStatus.get()
    if stagStausCheck == 1:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BC]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BD]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BE]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BF]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C0]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C1]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C2]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C3]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C4]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C5]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C6]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C7]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC50]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC51]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC54]), 1)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC58]), 1)
        
    else:
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BC]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BD]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BE]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4BF]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C0]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C1]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C2]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C3]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C4]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C5]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C6]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x4C7]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC50]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC51]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC54]), 0)
        pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xC58]), 0)

def save():
    new_geo = int(geoEntry.get())
    pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0x1C4]), new_geo)
    tkinter.messagebox.showinfo("Success", "Changes saved successfully")   
    #print("inf")
    #pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF4]), 1)
    invincibility()
    infJump()
    infSoul()
    #pm.write_int(getPointerAddress(gameModule+0x019B8900, offsets=[0x0, 0xD8, 0x268, 0xC8, 0xBF3]), 1)
    unlockAllAbilites()
    unlockAllMaps()
    unlockAllStagsTrams()
    allCharms()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)
        editMenu = Menu(menu)
        editMenu.add_command(label="Light Mode", command=self.L_mode)
        editMenu.add_command(label="Dark Mode", command=self.D_mode)
        menu.add_cascade(label="Theme", menu=editMenu)
    def L_mode(self):
        sv_ttk.set_theme("light")
    def D_mode(self):
        sv_ttk.set_theme("dark")

root = Tk()
app = Window(root)
#root.overrideredirect(True)
root.title("Hollow Knight Trainer")
sv_ttk.set_theme("light")
root.resizable = False

# themeSwitch = ttk.Checkbutton(text="Theme", style='Switch.TCheckbutton')
# themeSwitch.grid(column=1, row=14, pady=10)

loadProcessBtn = ttk.Button(text="Load Process", width=41, command=loadProcess, style="Accent.TButton")
loadProcessBtn.grid(column=0, row=0, pady=10, columnspan=2)

labelframe = ttk.LabelFrame(root, text="Options", width=35, height=300)
labelframe.grid(column=0, row=1, padx=20,pady=10, columnspan=2)

labelframe2 = ttk.LabelFrame(root, text="Misc.", width=35, height=300)
labelframe2.grid(column=0, row=7, padx=20, pady=10, columnspan=2)
 
geoLbl = ttk.Label(labelframe, text="Geo:")
geoLbl.grid(column=0, row=2, padx=10, sticky="w")

geoEntry = ttk.Entry(labelframe, width=33, state="disabled")
geoEntry.grid(column=1, row=2, padx=10, pady=10)

invincibilityStatus = tkinter.IntVar()
invincibilityCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Invincibility", variable=invincibilityStatus)
invincibilityCheck.grid(column=0,padx=10, row=4)

infJumpStatus = tkinter.IntVar()
infJumpCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Infinite Jump", variable=infJumpStatus)
infJumpCheck.grid(column=0,padx=10, row=5)

infSoulStatus = tkinter.IntVar()
infSoulCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Infinite Soul", variable=infSoulStatus)
infSoulCheck.grid(column=0,padx=10, row=6)

abilityStatus = tkinter.IntVar()
abilityCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Unlock All Abilities", variable=abilityStatus)
abilityCheck.grid(column=0,padx=10, row=7)

mapStatus = tkinter.IntVar()
mapCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Unlock All Maps", variable=mapStatus)
mapCheck.grid(column=0,padx=10, row=8)

allCharmsStatus = tkinter.IntVar()
allCharmsCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Unlock All Charms", variable = allCharmsStatus)
allCharmsCheck.grid(column=0,padx=10, row=9)

stagStatus = tkinter.IntVar()
stagCheck = ttk.Checkbutton(labelframe2, state="disabled", width=35, text="Unlock All Stags & Trams", variable=stagStatus)
stagCheck.grid(column=0,padx=10, row=10)

noneStatus = tkinter.IntVar()
noneCheck = ttk.Label(labelframe2,text="")
noneCheck.grid(column=0,padx=10, row=11)

saveBtn = ttk.Button(root, text="Save", state="disabled", command=save)
saveBtn.grid(column=0, row=13, columnspan=2, pady=10)
 
root.mainloop()