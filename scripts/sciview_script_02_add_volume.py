# @SciView sv
# @Dataset img

"""
This script adds an open image to sciview as a volume.

 The lines on top ensure we have access to:
 - sv: a running sciview instance (will launch it if none exists)
 - img: an open image
"""

import org.joml.Vector3f as Vector3f

# adding the image as a volume to sciview
volume = sv.addVolume(img, "Volume")

# setting the initial scale of the volume
volume.setScale(Vector3f(1, 1, 1))

print("done")