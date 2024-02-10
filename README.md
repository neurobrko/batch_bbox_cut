# Batch Bounding Box Cutter with extended functionality
#### Written for [domased.sk](https://domased.sk/)
**Author:** Marek Paulík | elvis@elvis.sk

## Description
Script for cutting out white bounding box of images in specified folder with simple progress bar indicating running of the script.
Few settings can be tweaked either by editing _preferences.py_ or with command line arguments.
For now (1.0.08) those are: custom bounding box, overwriting (or not) original files and toggle welcome message.

## Usage
CLI arguments overrides _preferences.py_ therefore it is recommended to use _preferences.py_ for default settings and CLI arguments for per use tweaks.  
File _preferences.py_ contains all settings, only some can be changed with CLI arguments.

### preferences.py
***extList*** Contains file extensions to be processed. Currently tested only with _jpg_ and _jpeg_. Specify extensions in lowercase. Also uppercase extensions will be processed.<br>
***welcomeMsg*** Turns on or off Welcome message.<br>
***overwrite*** If True, the original files will be overwritten. If False, new directory specified by _processedDir_ will be created (if it doesn't exist) and new files will be written there. Directory is created in the same direcotry as original files.<br>
***processedDir*** See _overwrite_<br>
***boundingBox*** You can set custom bounding box as list: \[left, top, right, bottom\]<br>
***prefix*** Add prefix to new filename.<sup>_WARN_</sup><br>
***pfxSeparator*** Separator between prefix and filename. If prefix is not specified, separator is ignored.<sup>_WARN_</sup><br>
***suffix*** Add suffix to new filename.<sup>_WARN_</sup><br>
***sfxSeparator*** Separator between filename and suffix. If suffix is not specified, separator is ignored.<sup>_WARN_</sup><br>
***ppi*** Change resolution of processed image to specified value. Will not change if set to 0.

<sup>***WARN***</sup> _Prefix, suffix and separators are ignored if overwrite is active! Please use valid characters in filenames, there is no filename validation implemented yet!_

### Command line arguments
-h | **Help:** Prints out help.<br>
-d | **Path to directory:** If not specified with -d flag the script will prompt you. You can use both full or relative path.<br>
-b | **Bounding Box:** If only one number is supplied, all sides will be set same. If you want each side different supply four numbers separated with comas, without spaces.
-o | **Overwrite:** Overwrite original images. If both _-n_ and _-o_ are specified by accident, _-o_ is ignored.<br>
-n | **No overwrite:** Do not overwrite original images. Directory name for processed images must be supplied.<br>
-p | **Resolution:** Change resolution to specified ppi value.<br>
-a | **Prefix:** Add prefix to filename.<sup>_WARN_</sup><br>
-A | **Prefix separator** Separator between _prefix_ and _filename_.<sup>_WARN_</sup><br>
-z | **Suffix:** Add suffix to filename.<sup>_WARN_</sup><br>
-Z | **Suffix separator** Separator between _filename_ and _prefix_.<sup>_WARN_</sup><br>
-w | **Welcome message:** Turn on/off Welcome message.<br>

<sup>***WARN***</sup> _Prefix, suffix and separators are ignored if overwrite is active! Please use valid characters in filenames, there is no filename validation implemented yet!_

## TO DO
- [ ] resize image with longer edge according to specified size
- [ ] print some useful report on exit
- [ ] add validation to resolution
- [ ] add some validation to prefix, suffix and separators
- [ ] internalization (slovak and english)
