from os import system
import sys
from .trashlib import Message, move, parseArguments, pwd, checkArgs, currentTime, writeToFile, listdir, exists

def trash():
    TRASH_INFO="/home/ashtamkar/.local/share/Trash/info"
    TRASH_FILES="/home/ashtamkar/.local/share/Trash/files"

    argsCorrect, argc ,data = checkArgs(1,2)
    command = None

    if not argsCorrect:
        print(f"{data} \n\n USAGE: \n\ttrash --add <filename>\n\ttrash --restore <filename>\n\ttrash --show")
        exit(1)

    version = lambda *args: print("Trash-It. \nVersion 1.0\n\nThis is free software; you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.")


    def add(fileName):

        if not exists(f"{pwd}/{fileName}"):
            print("File Does not Exist.")
            exit(126)

        else:
            Date, Time = currentTime.split()
            Time = Time.split('.')[0]

            data = f"[Trash Info]\nPath={pwd}/{fileName.replace(' ', '%20')}\nDeletionDate={Date}T{Time}"

            success = writeToFile(
                fileName=f"{TRASH_INFO}/{fileName}.trashinfo",
                data=data,
                mode='w'
            )

            if success:
                move(f"{pwd}/'{fileName}'", f"{TRASH_FILES}/")
                print(f"Trashed {fileName}")
            else:
                print("Some Error Occured. Please check manually to find the fault.")

    def show(*args):
        trashedFiles = listdir(f"{TRASH_FILES}")
        if len(trashedFiles) > 0:
            print("The files in the Trash are :- ")
            for i, fileName in enumerate(trashedFiles):
                print(f" {f'{i+1}.':<4} {fileName}")
            return trashedFiles
        else:
            print("No files in Trash.")
            return None

    def restore(fileName):
        trashedFiles = listdir(TRASH_FILES)

        if fileName not in trashedFiles:
            print(f"{fileName} not found in Trash.")
            exit(1)
        else:
            filePath = None
            
            with open(f"{TRASH_INFO}/{fileName}.trashinfo") as trashFile:
                filePath = trashFile.readlines()[1].split('=')[1].replace('%20', '\\ ')
                move(f"{TRASH_FILES}/'{fileName}'", filePath)
            
            system(f"rm {TRASH_INFO}/'{fileName}'.trashinfo")

            print(f"{fileName} restored. ")



    def restoreAll(*args):
        trashFiles = listdir(TRASH_FILES)
        print()
        if show() == None:
            print("Nothing to Restore.")
            exit(0)
        elif input(f"\nDo you wish to restore all the above files ?\n\nEnter choice (yes\\no): ").strip().lower()[0] != 'y': 
            print("\nNothing Changed.")
            exit(1)
        else:
            for file in trashFiles:
                restore(file)
            Message.success("All files restore complete.")

    def helpMessage(*args)-> None:
        version()
        print("\nUSAGE   : trash <options> [<fileName1>,<fileName1>,<fileName1>]")
        print("\nOptions Available : ")
        for command in COMMANDS_INFO:
            print(command, COMMANDS_INFO[command])
        print("\n EXAMPLE :\n\ttrash --help\n\ttrash --add file1.xyz file2.xyz file3.png ...")
        


    AVAILABLE_COMMANDS =  {
        'show'       :show,
        'help'       :helpMessage,
        'restore-all':restoreAll,
        'v'          :version,
        'version'    :version,
        'add'       :add,
        'restore'   :restore,
    }
    COMMANDS_INFO =  {
        '-v    --version      '       :"Display Version Information of Command",
        '-h    --help         '       :"Display this HELP message.",
        '-a    --add          '       :"Add Files to the Trash",
        '-s    --show         '       :"Show all the files and folders, currently in trash.",
        '      --restore      '       :"Restore some files from the Trash.",
        '      --restore-all  '       :"Restore ALL the files and folders currently in trash.",
    }

    arguments = parseArguments()
    options   = arguments['options']
    files     = arguments['parameters']

    if len(options) == 0:
        if len(files) > 0: 
            options.append('add')
        else:
            Message.error("No files/folders, nor options provided. For more details, type : \n\t trash --help")

    if len(options) == 1:
        options = options[0].lstrip('-')
        command = AVAILABLE_COMMANDS.get(options)
        
        if options in ('add', 'restore'):
            #Only Raise ERROR if No Files given Input
            if len(files) == 0:
                Message.error(" --add and --restore options take atleast one input file/folder.")
                command = lambda *args :exit(126)
        else:
            #Only Raise a WARNING if any Files given Input
            if len(files) != 0:
                Message.warning("--show and --restore-all options take no input files/folders. \nIgnoring...")
    else:
        Message.error("Too many options.")

    print()

    if command == None:
        Message.error("")
        command = lambda *args :exit(130)

    elif command in (add, restore):
        for file in files:
            command(file)
    else:
        command(files)
