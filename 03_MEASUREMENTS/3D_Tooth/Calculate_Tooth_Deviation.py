import math
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
import csv

'''
Calculating the 3 dimensional maximal, minimal and the span from max to min deviation between the pointcloud and the CAD model
'''

def calculate_center(pointcloud):
    with open(pointcloud, 'r') as file:
        pc = []
        for line in file:
            x, y, z = map(float, line.split())
            pc.append((x, y, z))


    total_points = len(pc)
    sum_x = sum_y = sum_z = 0.0
    for point in pc:
        x, y, z = point
        sum_x += x
        sum_y += y
        sum_z += z
    center_x = sum_x / total_points
    center_y = sum_y / total_points
    center_z = sum_z / total_points

    return center_x, center_y, center_z


def calculate_angle(point, center):
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    angle = math.atan2(dy, dx)
    if angle < 0:
        angle += 2 * math.pi
    angle_degrees = math.degrees(angle)
    return angle_degrees



def calculate_tooth_deviation(pointcloud, CAD, num_teeth):
    max = 0
    min = math.inf

    for tooth in range(1, num_teeth+1):
        tooth_pc = get_current_tooth(pointcloud, tooth, num_teeth)
        tooth_CAD = get_current_tooth(CAD, tooth, num_teeth)

        for point1, point2 in zip(tooth_pc, tooth_CAD):
            x1, y1, z1 = point1
            x2, y2, z2 = point2
            diff = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
            # print(diff)
            if max < diff:
                max = diff

            if min > diff:
                min = diff

    span = max - min
    return max, min, span

def get_current_tooth(pointcloud, tooth, num_teeth):
    corridor_angle = ((tooth - 0.75)*360 / num_teeth, (tooth + 0.25) * 360 / num_teeth)
    center = calculate_center(pointcloud)
    with open(pointcloud, 'r') as file:
        lines = file.readlines()

        # Extract coordinates within area
        points = []
        for line in lines:
            x, y, z = map(float, line.split())

            angle = calculate_angle((1000*x, 1000*z), (1000*center[0], 1000*center[2]))

            if corridor_angle[0] <= angle <= corridor_angle[1]:
                points.append([x, y, z])
    '''
    if tooth == 1000000:
        # Extract x, y, and z coordinates from the points
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] for point in points]

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Scatter plot of the points
        ax.scatter(x, y, z)

        # Set labels for each axis
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Display the plot
        plt.show()
    '''
    return np.array(points)

def calculate_folder(folder_path, CAD,  num_teeth, output_file):
    # Open output CSV in write mode
    with open(output_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        # Write header row
        writer.writerow(['File', 'max_Deviation', 'min_Deviation', 'span_Deviation'])

        # Iterate through folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            print(f"Calculating file {filename}")

            # Check if path is file
            if os.path.isfile(file_path):
                # Call tooth deviation
                output = calculate_tooth_deviation(file_path, CAD, num_teeth)

                # Write to csv
                writer.writerow([filename, output[0], output[1], output[2]])

dir_in = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(dir_in, '../../01_DATA/Z19/PointClouds/.xyz')
CAD_path = os.path.join(dir_in, '../../01_DATA/Z19/PointClouds/cutCAD_Z19.xyz')

calculate_folder(folder_path, CAD_path, 19, 'z19_tooth_deviation.csv')
