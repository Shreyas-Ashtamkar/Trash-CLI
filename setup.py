from setuptools import setup

long_description = """

# Native Trash CLI - V1.0

This is free software; you are free to change and redistribute it.<br/>
There is NO WARRANTY, to the extent permitted by law.


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

"""
setup(
	name='Trash-CLI',
	version='0.1.0',
	description='A Python Built Package for Sendign Files to Trash.',
	py_modules=[],
	package_dir={'':'src'},
    author="Shreyas Ashtamkar",
    author_email="shreyu@programmer.net",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)