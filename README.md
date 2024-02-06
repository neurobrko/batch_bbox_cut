# Batch Bounding Box Cutter with extended functionality
#### Written for domased.sk by Marek Paulík.

## Description
Script for cutting out white bounding box of images in specified folder.
Few settings can be tweaked either by editing _preferences.py_ or with command line arguments.
For now (1.0.01) those are: custom bounding box and overwriting og original files.

## Usage
CLI arguments overrides _preferences.py_ therefore it is recommended to use _preferences.py_ for default settings and CLI arguments for per use tweaks.  
File _preferences.py_ contains all settings, only some can be changed with CLI arguments.

### preferences.py
_extlist_ contains file extensions to be processed. Currently tested only with _jpg_ and _jpeg_. Specify extensions in lowercase. Also uppercase extensions will be processed.

**Help:** -h | Prints out help.  
**Welcome message:** -w | Turn on/off Welcome message.
**Path to directory:** -d | If not specified with -d flag the script will prompt you. You can use both full or relative path.  
**Bounding Box:** -b | If only one number is supplied, all sides will be set to it. If you want each side different supply four numberes separated with comas, without spaces.
