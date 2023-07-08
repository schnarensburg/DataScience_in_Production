import os
import csv

def remove_y(data):
    return [[x, z] for x, y, z in data]

dir_in = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(dir_in, '../01_DATA/Z13/cutCAD_3D_Z13.txt')

dir_out = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(dir_out, '../01_DATA/Z13/cutCAD_2D_Z13.txt')

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # Read the contents of the input file
        with open(os.path.join(input_folder, filename), 'r') as file:
            lines = file.readlines()

        # Remove first and last line and the y-coordinate
        selected_lines = lines[1:-1]
        points = [[float(x) for x in line.split()] for line in selected_lines]
        points = remove_y(points)

        output_filename = os.path.splitext(filename)[0] + '_2D.txt'
        with open(os.path.join(output_folder, output_filename), 'w') as file:
            for point in points:
                file.write(f"{point[0]} {point[1]}\n")