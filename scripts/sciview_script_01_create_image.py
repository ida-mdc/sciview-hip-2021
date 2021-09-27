# @UIService ui

"""
This script generates a 3D image and displays it in ImageJ.

The line on the very top ensures we have access to:
- ui: the UIService for displaying data
"""

import net.imglib2.img.array.ArrayImgs as ArrayImgs

# specifying the size of the image to be created
w = 100
h = w
d = w

# creating an image of type unsigned byte 
img = ArrayImgs.unsignedBytes(w, h, d)

# creating access to the pixels of the image
img_ra = img.randomAccess()

# iterating over all pixel positions in x direction
for x in range(0, w):

	# iterating over all pixel positions in y direction
	for y in range(0, h):

		# iterating over all pixel positions in z direction
		for z in range(0, d):

			# calculating the pixel value for the current position
			x0 = x - 50
			y0 = y - 50
			z0 = z - 50
			val = 255 - (x0**2 + y0**2 + z0**2) ** 0.65

			# setting the pixel value for the current position
			img_ra.setPositionAndGet([x, y, z]).setReal(val)

# display image
ui.show("input", img)
