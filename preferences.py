# Options marked with *-* can be overridden from CLI

# List of fileptypes to process
extList = ["jpg", "jpeg"]

# *-* Display Welcome message
welcomeMsg = False

# *-* Overwrite original picture or put it in processedDir directory
overwrite = False
processedDir = "processed"

# *-* Specify bounding box (left, top, right, bottom)
boundingBox = [0, 0, 0, 0]

# *-* Specify final image size according to format of the cropped image
portraitSize = [980, 750]
landscapeSize = [600, 750]

# *-* Ignore all bounding box settings and add none
noBoundingBox = False

# *-* Specify ammount of precut on all sides in percents. 0 means no precut.
precut = 15

# *-* File naming
prefix = ""
pfxSeparator = "_"
suffix = ""
sfxSeparator = "_"

# *-* Change resolution. 0 means no change.
ppi = 0

# *-* Resize specified side to specified dimension. 0 means no resizing.
resize = {"side": "x", "dimension": 750}

# *-* amount of brightness to enhance picture before calculating bounding box. 0 means no enhancement.
brightness = 1.5

