# Trash-it - V1.0

A Simple, command line utility to safely put the files/folders to the bin. 
(A Safer way than rm command. )

Have you ever deleted the wrong files by `rm` which were not backed up ? Have you felt that Panic ? That eagerness to bring back the files that have been lost ? 

If yes, or no, anyways, I have a tool, which can be verry usefull to you. (*can*)

## USAGE


`USAGE   : trash <options> [<fileName1>,<fileName1>,<fileName1>]`


## Options Available :


| Short |     Options       |                Description                                   |
| ----- | ----------------- | ------------------------------------------------------------ |
| `-v`  |   `--version`     |  Display Version Information of Command<br>                  |
| `-h`  |   `--help`        |  Display this HELP message.<br>                              |
| `-a`  |   `--add`         |  Add Files to the Trash<br>                                  |
| `-s`  |   `--show`        |  Show all the files and folders, currently in trash.<br>     |
|       |   `--restore`     |  Restore some files from the Trash.<br>                      |
|       |   `--restore-all` |  Restore ALL the files and folders currently in trash.<br>   |

## EXAMPLE :


```shell
trash --help
```
```shell
trash --add file1.xyz file2.xyz file3.png ...
```
## NOTE : 

This is free software; you are free to change and redistribute it.<br/>
There is NO WARRANTY, to the extent permitted by law.
