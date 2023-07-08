import os
from stl import mesh
import numpy as np

def stl_to_xyz(stl_file):
    # Load the STL file
    mesh_data = mesh.Mesh.from_file(stl_file)

    # Extract vertices from the mesh
    vertices = mesh_data.vectors.reshape(-1, 3)

    # Output XYZ file path
    xyz_file = os.path.splitext(stl_file)[0] + '.xyz'

    # Save vertices to XYZ file
    np.savetxt(xyz_file, vertices, delimiter=' ', fmt='%.6f')
    print(f"XYZ file saved: {xyz_file}")

# Usage example
stl_file_path = '/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z13/PointClouds/cutCAD_Z13.xyz'
stl_to_xyz(stl_file_path)
