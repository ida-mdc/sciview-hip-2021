# @Dataset img
# @SciView sv

"""
This script generates a mesh from an open 3D image and adds it to sciview.

The lines on the very top ensure we have access to:
- sv: a running sciview instance
- img: an open image
"""

import net.imagej.mesh.Meshes as Meshes
import sc.iview.process.MeshConverter as MeshConverter

# generate the mesh from a 3D image using the marching cubes algorithm
# the second parameter determines the pixel value distinguishing foreground and background
mesh = Meshes.marchingCubes(img, 100)

# convert the mesh into a mesh object compatible to sciview
sv_mesh = MeshConverter.toScenery(mesh, False, True)

# name the mesh (useful for replacing it)
sv_mesh.setName("Mesh")

# find volume added in script 02
volume = sv.find("Volume")

# in case you ran this script before, remove the existing mesh
volume.removeChild("Mesh")

# add the mesh as a child to the volume to make them stick together
volume.addChild(sv_mesh)

print("done")