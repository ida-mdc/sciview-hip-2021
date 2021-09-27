# @Dataset img
# @SciView sv

"""
This script generates a mesh from an open 3D image,
saves it to disk as STL and adds it to sciview.

The lines on the very top ensure we have access to:
- sv: a running sciview instance
- img: an open image
"""

import net.imagej.mesh.Meshes as Meshes
import sc.iview.process.MeshConverter as MeshConverter
import sc.iview.Utils as Utils

# locate the mesh added to the volume in script 05
sv_mesh = sv.find("Volume").getChildrenByName("Mesh")[0]

# save the mesh to disk as STL
Utils.writeSCMesh("mesh.stl", sv_mesh)

print("done")