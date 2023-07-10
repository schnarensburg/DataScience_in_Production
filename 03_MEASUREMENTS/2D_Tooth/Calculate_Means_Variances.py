import math
import os
import re

import numpy as np
import csv

'''
Calculating the mean deviation (+variance) of a tooth from the CAD model by cutting the gear into 13/19 slices and comparing each coordinate with the CAD file
'''

def calculate_means(txt2D_folder, file_CAD, num_teeth):
    means_array = []
    file_list = os.listdir(txt2D_folder)

    for file in file_list:
        file_name = os.path.join(txt2D_folder, file)

        sum_mean = 0
        for tooth in range(1, num_teeth + 1):
            tooth_pc = get_current_tooth(file_name, tooth, num_teeth)
            tooth_CAD = get_current_tooth(file_CAD, tooth, num_teeth)
            for point1, point2 in zip(tooth_pc, tooth_CAD):
                x1, y1 = point1
                x2, y2 = point2
                sum_mean += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        mean = sum_mean / num_teeth
        means_array.append([file, mean])

    # print(f" Means: {means_array}")
    return means_array


def calculate_vars(txt2D_folder, file_CAD, means_array, num_teeth):
    vars_array = []
    file_list = os.listdir(txt2D_folder)

    for file in file_list:
        file_name = os.path.join(txt2D_folder, file)

        sum_var = 0
        for tooth in range(1, num_teeth + 1):
            tooth_pc = get_current_tooth(file_name, tooth, num_teeth)
            tooth_CAD = get_current_tooth(file_CAD, tooth, num_teeth)
            for point1, point2 in zip(tooth_pc, tooth_CAD):
                x1, y1 = point1
                x2, y2 = point2
                sum_var += (float(means_array[tooth][1]) - (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))) ** 2

        variance = sum_var / num_teeth
        vars_array.append([file, variance])

    # print(f" Variances: {vars_array}")
    return vars_array


def get_current_tooth(file, tooth, num_teeth):
    corridor_angle = ((tooth - 0.75) * 360 / num_teeth, (tooth + 0.25) * 360 / num_teeth)
    with open(file, 'r') as file:
        lines = file.readlines()

        # Extract X and Y for points within the area
        points = []

        for line in lines:
            x, y = map(float, line.split())
            angle = math.atan2(y, x)
            if angle < 0:
                angle += 2 * math.pi

            angle_degrees = math.degrees(angle)
            if corridor_angle[0] <= angle_degrees <= corridor_angle[1]:
                points.append([x, y])
    return np.array(points)

'''
def calculate_tooth_mean(tooth_pc, file_CAD):
    sum_mean = 0
    for point1, point2 in zip(tooth_pc, zCAD):
        x1, y1 = point1
        x2, y2 = point2
        sum_mean += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return sum_mean


def calculate_tooth_variance(tooth_pc, zCAD, mean):
    sum_var = 0
    for point1, point2 in zip(tooth_pc, zCAD):
        x1, y1 = point1
        x2, y2 = point2
        sum_var += (mean - math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 2
    return sum_var
'''

def sort_and_write_to_csv(means, variances, output_file_means, output_file_variances):
    means_sorted = sorted(means, key=lambda x: float(re.findall(r'\d+', x[0])[0]))
    variances_sorted = sorted(variances, key=lambda x: float(re.findall(r'\d+', x[0])[0]))

    with open(output_file_means, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Mean'])

        for mean in means_sorted:
            writer.writerow([mean[0], mean[1]])

    with open(output_file_variances, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Variance'])

        for var in variances_sorted:
            writer.writerow([var[0], var[1]])


txt2D_folder = '../../01_DATA/Z13/Reany_2D_Z13.txt'
file_CAD = '../..01_DATA/Z13/cutCAD_2D_Z13.txt'
num_teeth = 13

means = calculate_means(txt2D_folder, file_CAD, num_teeth)
variances = calculate_vars(txt2D_folder, file_CAD, means, num_teeth)
output_file_means = '../../07_RESULTS/2D_Analysis/meansZ13.csv'
output_file_variances = '../../07_RESULTS/2D_Analysis/results_variances_deviation_tooth_Z13.csv'
sort_and_write_to_csv(means, variances, output_file_means, output_file_variances)