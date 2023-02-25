import minecraft_launcher_lib
import subprocess
import os
import PySimpleGUI as sg

def start_game(gf_version):
    global minecraft_directory

    forge_version = minecraft_launcher_lib.forge.find_forge_version(gf_version)
    if forge_version is None:
        print("This Minecraft Version is not supported by Forge!")
        sg.popup("This Minecraft Version is not supported by Forge!")
        exit()

    sp_version = forge_version.split("-")
    print(forge_version)
    print(sp_version)
    version = sp_version[0]+"-forge-"+sp_version[1]
    print(version)

    if os.path.exists(minecraft_directory+"/versions/"+version) == False:
        minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory)




#Generate Test Options
    options = {"username": "Login Now!", "uuid": "0000", "token": "0000"}

#Get Minecraft Command
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)

#Start Minecraft
    subprocess.call(minecraft_command)


# Get the Minecraft Directory of your System
minecraft_directory = "minecraft"
av_version = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
print(av_version)

layout = [[sg.Text('Version:')],
                 [sg.InputText()],
                 [sg.Button("Start"), sg.Button("Cancel")]]

window = sg.Window('Minecraft Python Launcher', layout)

event, values = window.read()


gm_version = values[0]

if event == "Start":
    start_game(gm_version)
    window.close()


