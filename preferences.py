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

# Specify ammount of precut on all sides in percents. 0 means no precut.
precut = 15

# *-* File naming
prefix = ""
pfxSeparator = "_"
suffix = ""
sfxSeparator = "_"

# *-* Change resolution. 0 means no change.
ppi = 0

# *-* Resize longer side to specified dimension. 0 means no resizing.
size = 0

# amount of brightness to enhance picture before calculating bounding box. 0 means no enhancement.
brightness = 1.5

