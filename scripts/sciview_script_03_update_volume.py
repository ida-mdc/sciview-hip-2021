# @Dataset img
# @SciView sv

"""
This script modifies an open image and updates an existing volume in sciview with the new data.

The lines on the very top ensure we have access to:
- sv: a running sciview instance
- img: an open image
"""

import math
import random

# creating access to the pixels of the image
img_ra = img.randomAccess()

# creating three random values for messing with the image data
random_x = random.random()
random_y = random.random()
random_z = random.random()


# iterating over all pixel positions in x direction
for x in range(0, img.dimension(0)):

	# iterating over all pixel positions in y direction
	for y in range(0, img.dimension(1)):

		# iterating over all pixel positions in z direction
		for z in range(0, img.dimension(2)):

			# calculating the pixel value for the current position
			x0 = 50 - abs(50-x)
			y0 = 50 - abs(50-y)
			z0 = 50 - abs(50-z)
			val = abs(math.cos(x0*random_x)*50+math.cos(y0*random_y)*50+math.sin(z0*random_z)*50)

			# setting the pixel value for the current position
			img_ra.setPositionAndGet([x, y, z]).setReal(val)

# locate the volume that was already added to sciview in the second script
volume = sv.find("Volume")

# update the volume with the new image data
sv.updateVolume(img, volume.name, [1,1,1], volume)

print("done")