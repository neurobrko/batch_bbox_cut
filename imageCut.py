#!.venv/bin/python3

from preferences import *
from pathlib import Path
from PIL import Image, ImageOps
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
    help="Bounding box size. Single number to specify all, or four numbers (separated with comas without spaces - left,top,right,bottom) to specify each. ",
    metavar="0 | 0,0,0,0",
)
# ap.add_argument(
#     "-s",
#     "--resize",
#     help="Resize longer side to specified size in pixels.",
#     metavar="NUM",
# )
# ap.add_argument(
#     "-r", "--dpi", help="Change resolution to specified dpi.", metavar="NUM"
# )
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


# process directory path user input
def user_input():
    print("Choose path to directory. If leaved empty, current dir will be used.")
    print("")
    # if directory was not specified with argument, choose it with user input
    processDir = input("Directory path: ")
    # check if dirpath is correct
    if processDir == "":
        processDir = Path.cwd()
    else:
        if not Path(processDir).is_dir():
            print("Bad directory path!")
            print(
                "Double check your input or try running the script from its original directory."
            )
            quit()
    return processDir


# check if path is valid
if args["dir"]:
    if Path(args["dir"]).is_dir():
        processDir = args["dir"]
    elif Path(os.path.join(Path.cwd(), args["dir"])).is_dir():
        processDir = os.path.join(Path.cwd(), args["dir"])
    else:
        print("Bad directory path!")
        print("Try specifing directory manually.")
        processDir = user_input()
else:
    processDir = user_input()

# check overwriting of original images
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

# itterate over process folder
imgList = []
for img in extList:
    imgList.extend(glob.glob(os.path.join(processDir, img)))

for i, imgPath in enumerate(imgList):
    with Image.open(imgPath) as img:
        imgBase = os.path.basename(imgPath)
        # calculate custom bounding box
        imgCropBBox = ImageOps.invert(img).getbbox()
        imgCustomBBox = (
            imgCropBBox[0] - customBoundingBox[0],
            imgCropBBox[1] - customBoundingBox[1],
            imgCropBBox[2] + customBoundingBox[2],
            imgCropBBox[3] + customBoundingBox[3],
        )
        img = img.crop(imgCustomBBox)
        img.save(os.path.join(destPath, imgBase))

print("Finished!")
if len(imgList) < 2:
    exitMsg = "1 file was processed."
else:
    exitMsg = str(len(imgList)) + " files were processed."
print(exitMsg)
