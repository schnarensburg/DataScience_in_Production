import math
import os
import numpy as np
import statistics
from matplotlib import pyplot as plt


def measure_variance(txt2D_folder, Z13CAD):
    arithmetic_Mean = np.zeros(20)
    var = np.zeros(20)
    total_distances = np.zeros(13)
    file_list = os.listdir(txt2D_folder)

    i = 0
    for file_name in file_list:
        i += 1
        file_path = os.path.join(txt2D_folder, file_name)
        total_distance = 0
        j = 0
        for tooth in range(1, 13):
            j += 1
            tooth_data = get_current_tooth(file_path, j)
            tooth_CAD = get_current_tooth(Z13CAD, j) # Inefficient, every tooth is calculated 100 times, maybe save them in a loop before
            total_distance += calculate_distance(tooth_data, tooth_CAD)
            total_distances[i] = total_distance

        arithmetic_Mean[i] = statistics.mean(total_distances)
        var[i] = statistics.variance(total_distances)



    arithmetic_Mean = statistics.mean(total_distances)
    print(f'arithmetic Mean: {arithmetic_Mean}')
    var = statistics.variance(total_distances)
    print(f'variance: {var}')




def calculate_distance(tooth_data, tooth_CAD):
    distances = np.zeros((len(tooth_data), len(tooth_data)))

    for i in range(len(tooth_data)):
        for j in range(len(tooth_CAD)):
            distances[i, j] = np.linalg.norm(tooth_data[i] - tooth_CAD[j])
    total_distance = int(np.sum(distances))
    return total_distance

def get_current_tooth(file, j):
    corridor_angle = ((j+0.25) * 360/13, (j+1.25)*360/13)
    with open(file, 'r') as file:
        lines = file.readlines()

        # Extract X and Y for points within the area
        x_values = []
        y_values = []

        for line in lines:
            x, y = map(float, line.split())
            angle = math.atan2(y, x)
            if angle < 0:
                angle += 2 * math.pi

            angle_degrees = math.degrees(angle)
            if corridor_angle[0] <= angle_degrees <= corridor_angle[1]:
                x_values.append(x)
                y_values.append(y)

    # Plot the current tooth
    #plt.scatter(x_values, y_values, label='testing: get_current_tooth_sample')
    #plt.legend()
    #plt.show()
    return x_values, y_values


def main():
    txt2D_folder = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/.txt2D'
    Z13CAD = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/2dimZ13CAD.txt'

    measure_variance(txt2D_folder, Z13CAD)

if __name__ == '__main__':
    main()
