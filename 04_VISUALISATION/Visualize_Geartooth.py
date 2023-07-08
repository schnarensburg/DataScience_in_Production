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
    return teeth_data

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/2dimZ19CAD.txt")
gear_data = np.loadtxt(file_path, delimiter=',')

num_teeth = 13

teeth_data = isolate_teeth(gear_data, num_teeth)

for i, tooth_data in enumerate(teeth_data):
    x_values = tooth_data[:, 0]
    y_values = tooth_data[:, 1]

    plt.plot(x_values, y_values, label=f'Tooth {i+1}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Isolated Teeth')
plt.show()