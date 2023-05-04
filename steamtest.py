import os
import winreg
import shutil
import time

os.system('title Altify ~ Easy Alting on GMOD')
os.system('color a')
os.system('cls')
print("\n Welcome! This Python Script will Aide you in using gmod alts while remaining undetected. \n All this script does it deletes files within your gmod directory that servers use to track you. \n \n \n ")
time.sleep(0.333)
# Define the Steam app ID for Garry's Mod
APP_ID = 4000

# Find the Steam installation path from the Windows registry
steam_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
steam_path = winreg.QueryValueEx(steam_key, "SteamPath")[0]
steam_key.Close()

# Construct the path to the SteamApps folder
steamapps_path = os.path.join(steam_path, "SteamApps")

# Find the installation folder for Garry's Mod
gmod_path = os.path.join(steamapps_path, f"common/GarrysMod")

file_path = gmod_path
data_path = file_path + "/garrysmod/data"
cldb_path = file_path + "/garrysmod/cl.db"
client_path = file_path + "/garrysmod/cfg/client.vdf"
advdupe_path = file_path + "/garrysmod/data/advdupe2" #Define File paths within gmod


if os.path.isdir(gmod_path): #Check if gmod is installed
    print("╔═══════════════════════════•●•════════════════════════╗")
    print(" =======> Garry's Mod installation found!")
    print(file_path)
    print("              | PRESS ENTER TO CONTIUE |")
    input("╚════════════════════════════•●════════════════════════╝")
    print(" \n \n \n ")

    if os.path.exists(advdupe_path): #Check if advdupe is present
        backup = input("[DETECTED ADVANCEDUPE2] Woud you Like to Make a Backup of your dupes? \n 1)Yes 2)No: \n")
        if backup == str(1):
            print("Copying Files...")
            shutil.copytree(advdupe_path, 'advdupe2', dirs_exist_ok=True) #Copy files to new folder within the program
            print("Advanced Duplicator 2 successfully Backed up! \n \n \n")
    else:
        print("ADVANCED DUPE NOT FOUND!")
    time.sleep(0.5)

    print("╔════════════•●•═════════════════════════╗")
    print("{*} ==========> Removing data folder! (BAD)")
    print("╚════════════•●══════════════════════════╝")
    print(" ")
    print(" ")
    if os.path.exists(data_path): # CHECK IF DATA FOLDER EXISTS
        shutil.rmtree(data_path) # RMTREE TO DELETE FOLDERS
        print("REMOVED")
        print(" ")
        print(" ")
    else:
        print("{*} That folder doesn't exist, skippin'")
        print(" ")
        print(" ")

    time.sleep(0.5)
    print("╔════════════════════════•●•══════════════════════════════════╗")
    print(" {*} ==========> Removing cl.db (IDK WHAT IT IS BUT IT TRACK U)")
    print("╚════════════════════════•●═══════════════════════════════════╝")
    print(" ")
    print(" ")
    if os.path.exists(cldb_path): #CHECK IF CL.DB EXISTS
        os.remove(cldb_path) # OS.REMOVE TO REMOVE SINGLE FILES!
        print("REMOVED")
        print(" ")
        print(" ")
    else:
        print("{*} That file doesn't exist, skipping'")
        print(" ")
        print(" ")


    time.sleep(0.5)
    print("╔════════════════════════════════════•●•══════════════════════════════════╗")
    print("{*} ==========> REMOVING /cfg/client.vdf (IT TRACK YOU!!)")
    print("╚════════════════════════════════════•●═══════════════════════════════════╝")
    if os.path.exists(client_path):
        os.remove(client_path) #AGAIN USING os.remove for SINLGE files only
        print("REMOVED")
        print(" ")
        print(" ")
    else:
        print("{*} That file doesn't exist, skipping'")
        print(" ")
        print(" ")


    print("╰┈┈┈┈┈┈┈> DONE! SIMPLY RUN GMOD AGAIN WITH NEW ACCOUNT!! MAKE SURE TO CHANGE IP!")
    print("╰┈┈┈┈┈┈┈> DONE! SIMPLY RUN GMOD AGAIN WITH NEW ACCOUNT!! MAKE SURE TO CHANGE IP!")
    print("╰┈┈┈┈┈┈┈> DONE! SIMPLY RUN GMOD AGAIN WITH NEW ACCOUNT!! MAKE SURE TO CHANGE IP!")
    color_list = [    "COLOR 0",    "COLOR 1",    "COLOR 2",    "COLOR 3",    "COLOR 4",    "COLOR 5",    "COLOR 6",    "COLOR 7",    "COLOR 8",    "COLOR 9",    "COLOR A",    "COLOR B",    "COLOR C",    "COLOR D",    "COLOR E",    "COLOR F"]

    # Loop through the list of color codes
    for i in range(4):
        for color in color_list:
            time.sleep(0.1)
            os.system(color)


else:
    print("Garry's Mod not found in Steam library")
