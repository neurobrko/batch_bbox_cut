# Batch Bounding Box Cutter with extended functionality
#### Written for [domased.sk](https://domased.sk/)
**Author:** Marek Paulík | elvis@elvis.sk

## Description
Script for cutting out white (or light grey) bounding box of images in specified folder with simple progress bar indicating running of the script.
Few settings can be tweaked either by editing _preferences.py_ or with command line arguments.
## Version
1.1.01

## Usage
CLI arguments overrides _preferences.py_ therefore it is recommended to use _preferences.py_ for default settings and CLI arguments for per use tweaks.  
File _preferences.py_ contains all the settings, all of them can be changed with CLI arguments except for processed filetypes.

### preferences.py
***extList*** Contains file extensions to be processed. Currently tested only with _jpg_ and _jpeg_. Specify extensions in lowercase. Also uppercase extensions will be processed.<br>
***welcomeMsg*** Turns on or off Welcome message.<br>
***overwrite*** If True, the original files will be overwritten. If False, new directory specified by _processedDir_ will be created (if it doesn't exist) and new files will be written there. Directory is created in the same direcotry as original files.<br>
***processedDir*** See _overwrite_<br>
***boundingBox*** You can set custom bounding box as list: [left, top, right, bottom].<br>
***landscapeSize*** Final dimensions of image if cropped image is landscape. If *boundingBox* is specified other than 0, *landscapeSize* is ignored.<br>
***portraitSize*** Final dimensions of image if cropped image is portrait. If *boundingBox* is specified other than 0, *portraitSize* is ignored.<br>
***minimumBoundingBox*** If *landscapeSize* and *portraitSize* are specified, minimum bounding box can be specified to avoid cropped image being "stuck" to the sides. 
It's kind of a failsafe, so all the sides of mininum bounding box are the same.<br>
***noBoundingBox*** No bounding box is added ignoring *boundingBox*, *portraitSize* or *landscapeSize*.<br>
***precut*** You can cut sides of image before processing. Specified as integer for percents.<br>
***prefix*** Add prefix to new filename.<sup>_WARN_</sup><br>
***pfxSeparator*** Separator between prefix and filename. If prefix is not specified, separator is ignored.<sup>_WARN_</sup><br>
***suffix*** Add suffix to new filename.<sup>_WARN_</sup><br>
***sfxSeparator*** Separator between filename and suffix. If suffix is not specified, separator is ignored.<sup>_WARN_</sup><br>
***ppi*** Change resolution of processed image to specified value. Will not change if set to 0.<br>
***resize*** Resize image with specified side to specified dimension. If custom bounding box is specified, it will be added 
after resizing, therefore final dimensions of the image will be *resized size + bounding box*.<br>
***brightness*** Level of brightness enhancement to override gray background and/or shadows. Should be float over 1.0.

<sup>***WARN***</sup> _Prefix, suffix and separators are ignored if overwrite is active! Please use valid characters in filenames, there is no filename validation implemented yet!_

### Command line arguments
-h | **Help:** Prints out help.<br>
-d | **Path to directory:** If not specified with -d flag the script will prompt you. You can use both full or relative path.<br>
-b | **Bounding Box:** If only one number is supplied, all sides will be set same. If you want each side different supply four numbers separated with comas, without spaces.<br>
-x | **Landscape Size:** Final dimensions of image if cropped image is landscape. Also dimension of original image inside final image is specified.<br>
-y | **Portrait Size:** Final dimensions of image if cropped image is portrait. Also dimension of original image inside final image is specified.<br>
-m | **Minimum Bounding Box:** If *Lnadscape Size* and *Portrait Size* are specified, minimum bounding box can be specified to avoid cropped image being "stuck" to the sides.<br>  
-B | **No Bounding Box:** No bounding box is added ignoring *-b*, *-x* or *-y*.<br>
-c | **Precut:** You can cut sides of image before processing. Specified as integer for percents.<br>
-e | **Enhance:** Level of brightness enhancement to override gray background and/or shadows. Should be float over 1.0.<br>
-o | **Overwrite:** Overwrite original images. If both _-n_ and _-o_ are specified by accident, _-o_ is ignored.<br>
-n | **No overwrite:** Do not overwrite original images. Directory name for processed images must be supplied.<br>
-p | **Resolution:** Change resolution to specified ppi value.<br>
-r | **Resize** Resize specified side of the image to specified size. Custom bounding box is added after resizing. Specify as *CHAR,INT*, where CHAR is either *x* or *y* and INT is desired size.<br>
-a | **Prefix:** Add prefix to filename.<sup>_WARN_</sup><br>
-A | **Prefix separator** Separator between _prefix_ and _filename_.<sup>_WARN_</sup><br>
-z | **Suffix:** Add suffix to filename.<sup>_WARN_</sup><br>
-Z | **Suffix separator** Separator between _filename_ and _prefix_.<sup>_WARN_</sup><br>
-w | **Welcome message:** Turn on/off Welcome message.<br>

<sup>***WARN***</sup> _Prefix, suffix and separators are ignored if overwrite is active! Please use valid characters in filenames, there is no filename validation implemented yet!_

### Notes
There is too many conditions regarding custom bounding box, so it is strongly recommended to use *-B* flag in CLI or *noBoundingBox* variable if you don't want to add any bounding box.

## TO DO
- [ ] rewrite this README!
- [ ] add option not to crop bounding box, so the script can be used for resize/change of ppi/adding prefix & suffix only (-x)
bounding box added to specified dimensions. **PROBLEM:** Non-white background
- [ ] print some useful report on exit
- [ ] add some validation to prefix, suffix and separators regarding invalid characters
- [ ] GUI
- [ ] internalization (slovak and english) 
