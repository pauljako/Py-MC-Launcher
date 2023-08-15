import minecraft_launcher_lib
import subprocess
import os
import PySimpleGUI as sg
import re


def start_game(gf_version, forge, custom, vanilla):
    global minecraft_directory

    if forge:
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
           print("The newest Forge Version is not installed.")
           sg.popup("The newest Forge Version is not installed. Click Ok to install it.")
           minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory)
    elif vanilla:
        version = gf_version
        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
    elif custom:
        version = gf_version





#Generate Test Options
    options = {"username": "Login_Now", "uuid": "0000", "token": "0000"}

#Get Minecraft Command
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)

#Start Minecraft
    subprocess.call(minecraft_command)


# Get the Minecraft Directory of your System
folders = ["minecraft", minecraft_launcher_lib.utils.get_minecraft_directory()]
minecraft_directory = "minecraft"
av_version = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
print(av_version)
df_folder = minecraft_launcher_lib.utils.get_minecraft_directory()
sg.theme("DarkPurple7")
layout = [[sg.Text('Version:')],
                 [sg.InputText(default_text=minecraft_launcher_lib.utils.get_latest_version()["release"])],
                 [sg.Text("Minecraft Directory:")],
                 [sg.Combo(folders, default_value=df_folder)],
                 [sg.Radio("Forge", "mdl", default=True), sg.Radio("Custom", "mdl"), sg.Radio("Vanilla", "mdl")],
                 [sg.Button("Start"), sg.Button("Cancel")]]

window = sg.Window('Minecraft Python Launcher', layout)

while True:                             # The Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        exit()
    if event == "Start":
        gm_version = values[0]
        minecraft_directory = values[1]
        print(values)
        window.hide()
        start_game(gm_version, values[2], values[3], values[4])
        break


sg.popup("Minecraft Ended", auto_close=True, auto_close_duration=5)






