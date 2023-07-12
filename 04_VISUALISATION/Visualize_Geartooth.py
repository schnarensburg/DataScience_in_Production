import numpy as np
import matplotlib.pyplot as plt
import os

def isolate_teeth(gear_data, num_teeth):
    # Calculate angular spacing between teeth
    angular_spacing = 360 / num_teeth

    # Initialize list to store isolated teeth
    teeth_data = []
    # Iterate over each tooth
    for tooth_index in range(num_teeth):
        # Calculate start and end angles for the tooth
        start_angle = tooth_index * angular_spacing
        end_angle = (tooth_index + 1) * angular_spacing

        #Identify data points within the angular range of the tooth
        tooth_data = []
        for data_point in gear_data:
            angle = np.degrees(np.arctan2(data_point[1], data_point[0]))
            #Check if the angle falls within the tooth's range
            if start_angle <= angle < end_angle:
                tooth_data.append(data_point)
        teeth_data.append(tooth_data)
    return teeth_data

def visualize(teeth_data, index):
    data = teeth_data[index]

    # Extract x and y coordinates from the data
    x_data = [point[0] for point in data]
    y_data = [point[1] for point in data]
    plt.scatter(x_data, y_data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.show()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../01_DATA/Z19/cutCAD_2D_Z19.txt")
gear_data = np.loadtxt(file_path)

num_teeth = 19

teeth_data = isolate_teeth(gear_data, num_teeth)
visualize(teeth_data, 0)