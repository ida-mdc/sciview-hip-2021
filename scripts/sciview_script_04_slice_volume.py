# @SciView sv

"""
This script adds a slicing plane to sciview, cropping the previously added volume.

The line on the very top ensures we have access to:
- sv: a running sciview instance
"""

import graphics.scenery.volumes.SlicingPlane as SlicingPlane
import graphics.scenery.volumes.Volume as Volume
import org.joml.Vector3f as Vector3f

# get the volume we previously added to sciview in script 02
volume = sv.find("Volume")

# set the slicing mode of the volume to Cropping
volume.slicingMode = Volume.SlicingMode.Cropping

# add a box which will help us to move and rotate the slicing plane
box = sv.addBox(Vector3f(0, 0, 0), Vector3f(10, 10, 10))

# create a slicing plane
plane = SlicingPlane()

# add the plane to the box so it will follow it's transformations
box.addChild(plane)

# let the plane know it's supposed to slice our volume
plane.addTargetVolume(volume)

print("done")