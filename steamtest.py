import os
import winreg
import shutil
import time

os.system('title Altify ~ Make Alts Great Again')
os.system('color a')
os.system('cls')
print("Checking for GMOD Installation! \n \n")
time.sleep(1.6)

def doesgmodexist():

    # Define the Steam app ID for Garry's Mod
    APP_ID = 4000
    # Find the Steam installation path from the Windows registry
    steam_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
    steam_path = winreg.QueryValueEx(steam_key, "SteamPath")[0]
    steam_key.Close()
    # Construct the path to the SteamApps folder
    steamapps_path = os.path.join(steam_path, "SteamApps")
    # Find the installation folder for Garry's Mod
    global gmod_path
    gmod_path = os.path.join(steamapps_path, f"common/GarrysMod")
    if os.path.isdir(gmod_path):
        print("╔═══════════════════════════•●•════════════════════════╗")
        print(" {*} ======> Garry's Mod installation found!")
        print(gmod_path)
        print("              | PRESS ENTER TO CONTIUE |")
        input("╚════════════════════════════•●════════════════════════╝ \n")
        return True
    else:
        print("GMOD NOT FOUND YOU NEED GMOD INSTALLED!")
        return False
        time.sleep(2)

##CHECK TO SEE IF GMOD EXIST

doesgmodexist()


def remove_folder(x):
    if os.path.exists(gmod_path + x): # CHECK IF DATA FOLDER EXISTS
        shutil.rmtree(gmod_path + x) # RMTREE TO DELETE FOLDERS
        print("╔════════════════════════════════════•●•══════════════════════════════════╗")
        print("        {*} ==========> Removed Folder ", x)
        print("╚════════════════════════════════════•●═══════════════════════════════════╝ \n")
    else:
        print("{*} ", x, " Doesn't Exist!")



def remove_file(x):
    if os.path.exists(gmod_path + x): #CHECK IF CL.DB EXISTS
        os.remove(gmod_path + x) # OS.REMOVE TO REMOVE SINGLE FILES!
        print("╔════════════════════════════════════•●•══════════════════════════════════╗")
        print("        {*} ==========> Removed File ", x)
        print("╚════════════════════════════════════•●═══════════════════════════════════╝ \n")
    else:
        print("{*} ", x, " Doesn't Exist!")



file_path = gmod_path
"/garrysmod/data"
"/garrysmod/cl.db"
"/garrysmod/cfg/client.vdf"

##CHECK ADVDUPE2

advdupe_path = file_path + "/garrysmod/data/advdupe2" #Define File paths within gmod
if os.path.exists(advdupe_path): #Check if advdupe is present
    backup = input("[DETECTED ADVANCEDUPE2] Woud you Like to Make a Backup of your dupes? \n 1)Yes 2)No: \n")
    if backup == str(1):
        print("Copying Files...")
        shutil.copytree(advdupe_path, 'advdupe2', dirs_exist_ok=True) #Copy files to new folder within the program
        print("Advanced Duplicator 2 successfully Backed up! \n \n \n")
else:
    print("ADVANCED DUPE NOT FOUND! Would you like to continue with the Removal Process?")
    input("Press Enter To continue!")
time.sleep(0.5)

##START REMOVING FILES



remove_folder("/garrysmod/cache/lua")
time.sleep(0.1)
remove_file("/garrysmod/cfg/config.cfg")
time.sleep(0.1)
remove_file("/garrysmod/cfg/client.vdf")
time.sleep(0.1)
remove_folder("/garrysmod/data")
time.sleep(0.1)
remove_folder("/garrysmod/materials")
time.sleep(0.1)
remove_folder("/garrsmod/media")
time.sleep(0.1)
remove_folder("/garrysmod/screenshots")
time.sleep(0.1)
remove_folder("/garrysmod/videos")
time.sleep(0.1)
remove_file("/garrysmod/cl.db")
time.sleep(0.1)
remove_file("/garrysmod/demoheader.tmp")
time.sleep(0.1)
remove_file("/garrysmod/GameState.txt")
time.sleep(0.1)
remove_file("/garrysmod/map.pack")
time.sleep(0.1)
remove_folder("/garrysmod/media")


print("╰┈┈┈┈┈┈┈> DONE! JUST RESTART GMOD!!")
print("╰┈┈┈┈┈┈┈> DONE! JUST RESTART GMOD!!")
print("╰┈┈┈┈┈┈┈> DONE! JUST RESTART GMOD!!")

color_list = [    "COLOR 0",    "COLOR 1",    "COLOR 2",    "COLOR 3",    "COLOR 4",    "COLOR 5",    "COLOR 6",    "COLOR 7",    "COLOR 8",    "COLOR 9",    "COLOR A",    "COLOR B",    "COLOR C",    "COLOR D",    "COLOR E",    "COLOR F"]

# Loop through the list of color codes
for i in range(4):
    for color in color_list:
        time.sleep(0.1)
        os.system(color)


