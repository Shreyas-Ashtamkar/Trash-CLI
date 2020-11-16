#!/usr/bin/python3

import sys,os

argList = sys.argv
argCount = len(argList)
programName = ''
commandName = ''

if argCount < 2 or argCount > 3:
    print("USAGE : convertProgram <programName> <commandName>;")
    exit(0)

if argCount >= 2:
    programName = argList[1]

if argCount == 3:
    commandName = argList[2]
else:
    commandName = (argList[1].split('.'))[0]

programName = f'{ os.getcwd() }/{ programName }'

inp = input(f"Creating a command named { commandName } from program { programName }. \n\n(Y\\N) : ")

if inp =='':
    inp = 'n'

inp = inp.lower()[0]

if inp == 'y':
    if os.path.exists(f'/home/ashtamkar/bin/{commandName}'):
        choice = input("The command exists. Do you wish to Re-Create it ? (Y\\N) [Default N] : ")
        if choice[0].lower() == 'y':
            os.system(f'rm /home/ashtamkar/bin/{commandName}')
        else:
            print("No Change..... Exiting ....")
            exit(0)
    os.system(f"ln -s {programName} /home/ashtamkar/bin/{commandName}")
    os.system(f"chmod u+x /home/ashtamkar/bin/{commandName}")
    print("\nTask Complete.")
elif inp == 'n':
    print("\nERROR : User Denied.")
else:
    print("\nERROR : Invalid Input.")

print("\n\n Exiting....")
