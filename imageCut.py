#!/usr/bin/env python

from preferences import *
from alive_progress import alive_bar
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import os
import argparse
import glob

# Create argument parser
ap = argparse.ArgumentParser()
ap.add_argument(
    "-d", "--dir", help="Path to directory with images to process.", metavar="PATH"
)
ap.add_argument(
    "-b",
    "--bbox",
    help="Bounding box size. Single number to specify all, or four numbers (separated with comas " 
         "without spaces - left,top,right,bottom) to specify each.",
    metavar="0 | 0,0,0,0",
)
ap.add_argument(
    "-c",
    "--precut",
    help="Cut image border before processing to get rid of artifacts in corners or sides of image. Value in percents.",
    metavar="INT",
)
ap.add_argument(
    "-e",
    "--enhance",
    help="Enhance brightness while processing to override gray background. Final image is saved without enhancement."
         "Value of 1.0 and greater. 0 for no enhancement.",
    metavar="FLOAT",
)
ap.add_argument(
    "-o",
    "--overwrite",
    help="Overwrite original images. Prefix and suffix are not applied.",
    action="store_true",
)
ap.add_argument(
    "-n",
    "--nooverwrite",
    help="Do not overwrite original files and save copies to specified directory in original directory. " 
         "Will be created if needed.",
    metavar="DIRNAME",
)
ap.add_argument(
    "-p", "--ppi", help="Change resolution to specified dpi.", metavar="INT"
)
ap.add_argument(
    "-s",
    "--size",
    help="Resize longer side to specified size in pixels.",
    metavar="INT",
)
ap.add_argument(
    "-a",
    "--prefix",
    help="Specified prefix will be added to processed filename if overwrite is not applied.",
    metavar="PFX",
)
ap.add_argument(
    "-A",
    "--pfxseparator",
    help="Separator between prefix and filename.",
    metavar="CHARS",
)
ap.add_argument(
    "-z",
    "--suffix",
    help="Specified suffix will be added to processed filename if overwrite is not applied.",
    metavar="SFX",
)
ap.add_argument(
    "-Z",
    "--sfxseparator",
    help="Separator between filename and suffix.",
    metavar="CHARS",
)
ap.add_argument(
    "-w",
    "--welcome",
    action="store_true",
    help="Display welcome message on script startup.",
)

# retrieve arguments
args = vars(ap.parse_args())

if args["welcome"] or welcomeMsg:
    print("***")
    print("* ### BATCH BOUNDING BOX CROP ###")
    print("* Made for www.domased.sk")
    print("* List of extensions to be processed: " + ", ".join(extList))
    print("* Behaviour of the script can be changed in variables.py,")
    print("* or with CLI arguments. Try running script with -h.")
    print("***")
    print("")

# Check if bounding box was specified in CLI, if not, use from preferences.py
if args["bbox"]:
    try:
        customBoundingBox = []
        cbbox = int(args["bbox"])
        for i in range(4):
            customBoundingBox.append(cbbox)
    except ValueError:
        try:
            customBoundingBox = []
            cbbox = args["bbox"].split(",")
            for i in range(len(cbbox)):
                customBoundingBox.append(int(cbbox[i]))
        except ValueError:
            print("Bad bounding box argument!")
            quit()
        except Exception as err:
            print("Something went wrong! (bbox from CLI / " + type(err).__name__ + ")")
            quit()

    if len(customBoundingBox) != 4:
        print("Bounding box count error!")
        print(customBoundingBox)
        quit()

try:
    customBoundingBox
except NameError:
    customBoundingBox = boundingBox
except Exception as err:
    print("Something went wrong! (bbox from preferences / " + type(err).__name__ + ")")
    quit()

# check if precut was specified in CLI
if args["precut"]:
    try:
        precut = int(args["precut"])
    except ValueError:
        print("Precut argument must be integer!")
        quit()
    except Exception as err:
        print("Something went wrong! (Precut from cli / " + type(err).__name__ + ")")
        quit()
    if not 0 <= precut <= 99:
        print("Precut must be between 1 and 99!")
        quit()

# check if engancement was specified in CLI
if args["enhance"]:
    try:
        brightness = float(args["enhance"])
    except ValueError:
        print("Brightness enhancement must be a float.")
        quit()
    except Exception as err:
        print("Something went wrong! (Brightness from cli / " + type(err).__name__ + ")")
        quit()
    if brightness < 0:
        print("Brightness must be greater then 0.0!")
        quit()

# process directory path user input
def user_input():
    print("Choose path to directory. If leaved empty, current dir will be used.")
    print("")
    # if directory was not specified with argument, choose it with user input
    processdir = input("Directory path: ")
    # check if directory path is correct
    if processdir == "":
        processdir = Path.cwd()
    else:
        if not Path(processdir).is_dir():
            print("Bad directory path!")
            print(
                "Double check your input or try running the script from its original directory."
            )
            quit()
    return processdir


# check if path is valid
if args["dir"]:
    if Path(args["dir"]).is_dir():
        processDir = args["dir"]
    elif Path(os.path.join(Path.cwd(), args["dir"])).is_dir():
        processDir = os.path.join(Path.cwd(), args["dir"])
    else:
        print("Bad directory path!")
        print("Try specifying directory manually.")
        processDir = user_input()
else:
    processDir = user_input()

# check overwriting of original images
# reset overwrite and processedDir variables if specified from CLI
# Check -o first and -n after that. Thus, way if both are specified, nooverwrite has priority
if args["overwrite"]:
    overwrite = True
if args["nooverwrite"]:
    overwrite = False
    processedDir = args["nooverwrite"]

if not overwrite:
    destPath = os.path.join(processDir, processedDir)
    if not Path(destPath).is_dir():
        os.mkdir(destPath)
else:
    destPath = processDir

# modify list of extensions to suit glob()
for i in range(len(extList)):
    extList[i] = "*." + extList[i]
    extList.append(extList[i].upper())  # add uppercase extensions

# iterate over process folder
imgList = []
for img in extList:
    imgList.extend(glob.glob(os.path.join(processDir, img)))

# if overwrite is True, remove prefix and suffix with its separators
if overwrite:
    prefix = pfxSeparator = sfxSeparator = suffix = ""
else:
    # check if suffix and prefix and respective separators were specified in CLI.
    if args["prefix"]:
        prefix = args["prefix"]
    if args["pfxseparator"]:
        pfxSeparator = args["pfxseparator"]
    if args["sfxseparator"]:
        sfxSeparator = args["sfxseparator"]
    if args["suffix"]:
        suffix = args["suffix"]
    # remove prefix and/or suffix separators, if prefix and/or suffix is not defined
    if not prefix:
        pfxSeparator = ""
    if not suffix:
        sfxSeparator = ""

# check if resolution was specified in CLI
if args["ppi"]:
    ppi = int(args["ppi"])

# check if resize was set in CLI
if args["size"]:
    size = int(args["size"])
# if resize specified, create tuple for thumbnail()
if size:
    imgSize = (
        size - customBoundingBox[0] - customBoundingBox[2],
        size - customBoundingBox[1] - customBoundingBox[3],
    )

with alive_bar(len(imgList), bar="classic", spinner="dots") as bar:
    for i, imgPath in enumerate(imgList):
        with Image.open(imgPath) as img:
            # add prefix and suffix to filename
            imgFilename, imgExt = os.path.splitext(os.path.basename(imgPath))
            imgBase = (
                prefix + pfxSeparator + imgFilename + sfxSeparator + suffix + imgExt
            )
            # precut image if there is some artefacts on the sides or in the corners
            if precut:
                imgWidth, imgHeight = img.size
                precutBBox = (imgWidth/100*precut, imgHeight/100*precut, imgWidth - imgWidth/100*precut, imgHeight - imgHeight/100*precut)
                img = img.crop(precutBBox)

            # enhance image brightness to get rid of grey background
            if brightness:
                enhancer = ImageEnhance.Brightness(img)
                imgEnhanced = enhancer.enhance(brightness)
            else:
                imgEnhanced = img

            # invert image to correctly calculate cropbox
            imgCropBBox = ImageOps.invert(imgEnhanced).getbbox()

            # add custom bounding box
            imgCropBBox = (
                imgCropBBox[0] - customBoundingBox[0],
                imgCropBBox[1] - customBoundingBox[1],
                imgCropBBox[2] + customBoundingBox[2],
                imgCropBBox[3] + customBoundingBox[3]
            )

            # crop bounding box
            img = img.crop(imgCropBBox)

            # change size if defined
            if size:
                img.thumbnail(imgSize, resample=Image.LANCZOS, reducing_gap=2.0)

            # save image with changed ppi if specified
            saveFile = os.path.join(destPath, imgBase)
            if ppi:
                img.save(saveFile, dpi=(ppi, ppi))
            else:
                img.save(saveFile)
            bar()

if len(imgList) < 2:
    exitMsg = "1 file was processed."
else:
    exitMsg = str(len(imgList)) + " files were processed."
print(exitMsg)
print("Done!")
