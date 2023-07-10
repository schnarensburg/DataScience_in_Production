import os
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np

'''
Trying to isolate a gear by cutting 'inner' points 
'''


def filter_points_by_radius(point_cloud, inner_radius, center, output_file):
    with open(output_file, 'w') as file:
        for point in point_cloud:
            distance = ((center[0] - point[0])**2 + (center[1] - point[1])**2)**0.5
            if inner_radius <= distance:
                file.write(f"{point[0]} {point[1]}\n")

    return output_file

def plot_point_cloud(Z19CAD):
    # Read the contents of TXT file
    with open(Z19CAD, 'r') as file:
        lines = file.readlines()

    # Extract X and Y values
    x_values = []
    y_values = []
    for line in lines:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)

    # Plot the data
    plt.scatter(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('filtered Z19')
    plt.legend('')

dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '../../01_DATA/Z19/cutCAD_2D_Z19.txt')
inner_radius = 2.1
center = (0.29, 0.04)


point_cloud = np.loadtxt(file_path)
plt.figure()
filteredZ19CAD = filter_points_by_radius(point_cloud, inner_radius, center, 'filteredZ19CAD.txt')
plot_point_cloud(filteredZ19CAD)
plt.show()