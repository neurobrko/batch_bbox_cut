# Batch Bounding Box Cutter with extended functionality
#### Written for domased.sk by Marek Paulík.

## Description
Script for cutting out white bounding box of images in specified folder.
Few settings can be tweaked either by editing _preferences.py_ or with command line arguments.
For now (1.0.01) those are: custom bounding box and overwriting og original files.

## Usage
CLI arguments overrides _preferences.py_ therefore it is recommended to use _preferences.py_ for default settings and CLI arguments for per use tweaks.

_imageCut.py -h_ - prints out help
*Path to directory:* Specify with -d flag or without -d flag the script will prompt you.