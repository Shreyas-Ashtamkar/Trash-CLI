from os import system, getcwd, listdir
from os.path import exists
from sys import argv
import datetime
from colorama import Fore, Back


pwd=getcwd()
currentTime = str(datetime.datetime.now())

def move(src:str, dest:str)->int:
    return system(f"mv {src} {dest}")

def checkArgs(minNo:int=-1, maxNo:int=-1)-> tuple:
    if minNo == -1: minNo = 0
    if maxNo == -1: maxNo = minNo

    args = argv[1:]
    argc = len(args)
    data   = None
    
    if argc in range(minNo, maxNo+1):
        data = True, argc, args
    else:
        if argc > maxNo:
            data = True, argc,"Too less Arguments"
        else:
            data = True, argc,"Too many Arguments"
    
    return data

def parseArguments() -> dict:
    options     = []
    parameters  = []
    
    for arg in argv[1:]:
        if arg[0] == '-':
            options.append(arg)
        else:
            parameters.append(arg)
    return {
        'options'   :options, 
        'parameters':parameters
        }

def writeToFile(fileName:str=None, data:str=None, mode:str = 'a') -> None:
    if not fileName or not data: return False
    with open(fileName, mode) as file:
        file.write(data)
    
    return True

class Message:
    Color = {
        'fore' : {
            'red'       :Fore.RED,
            'yellow'    :Fore.YELLOW,
            'green'     :Fore.GREEN,
            'blue'      :Fore.BLUE,
            'white'     :Fore.WHITE,
            'black'     :Fore.BLACK,
        },
        'back' : {
            'red'       :Back.RED,
            'yellow'    :Back.YELLOW,
            'green'     :Back.GREEN,
            'blue'      :Back.BLUE,
            'white'     :Back.WHITE,
            'black'     :Back.BLACK,
        }
    }
    @staticmethod
    def colored(message:str, fontColor:str = None, backColor:str = None)-> None:
        fontColor = Message.Color['fore'].get(fontColor)
        backColor = Message.Color['back'].get(backColor)
        if not fontColor: fontColor = Fore.RESET
        if not backColor: backColor = Back.RESET
        print(fontColor, backColor, message, Back.RESET, Fore.RESET)
    @staticmethod
    def warning(message:str):
        print(Fore.RED, Back.LIGHTYELLOW_EX,"WARNING :"+Fore.LIGHTYELLOW_EX +Back.RESET,message,Fore.RESET)

    @staticmethod
    def error(message:str):
        print(Fore.LIGHTYELLOW_EX, Back.RED,"ERROR :"+Fore.LIGHTRED_EX + Back.RESET,message,Fore.RESET)
    
    @staticmethod
    def success(message:str):
        print(Fore.LIGHTGREEN_EX+"SUCCESS :", Fore.RESET, message, )