# Batch Bounding Box Cutter with extended functionality
#### Written for [domased.sk](https://domased.sk/)
**Author:** Marek Paulík | elvis@elvis.sk

## Description
Script for cutting out white bounding box of images in specified folder.
Few settings can be tweaked either by editing _preferences.py_ or with command line arguments.
For now (1.0.03) those are: custom bounding box and overwriting original files, turn on/off welcome message.

## Usage
CLI arguments overrides _preferences.py_ therefore it is recommended to use _preferences.py_ for default settings and CLI arguments for per use tweaks.  
File _preferences.py_ contains all settings, only some can be changed with CLI arguments.

### preferences.py
***extList*** Contains file extensions to be processed. Currently tested only with _jpg_ and _jpeg_. Specify extensions in lowercase. Also uppercase extensions will be processed.<br>
***welcomeMsg*** Turns on or off Welcome message.<br>
***overwrite*** If True, the original files will be overwritten. If False, new directory specified by _processedDir_ will be created (if it doesn't exist) and new files will be written there. Directory is created in the same direcotry as original files.<br>
***processedDir*** See _overwrite_<br>
***boundingBox*** You can set custom bounding box as list: \[left, top, right, bottom\]

### Command line arguments
-h | **Help:** Prints out help.<br>
-w | **Welcome message:** Turn on/off Welcome message.<br>
-d | **Path to directory:** If not specified with -d flag the script will prompt you. You can use both full or relative path.<br>
-b | **Bounding Box:** If only one number is supplied, all sides will be set to it. If you want each side different supply four numbers separated with comas, without spaces.

## TO DO
- [ ] progress bar
- [ ] add prefix and/or suffix to new filename
- [ ] resize image with longer edge according to specified size
- [ ] resample image to specified resolution
- [ ] add CLI argument for overwrite
- [ ] internalization (slovak and english)
