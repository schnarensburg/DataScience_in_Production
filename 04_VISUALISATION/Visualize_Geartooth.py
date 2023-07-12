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
        print(tooth_data)
        teeth_data.append(tooth_data)
    return teeth_data

def visualize(teeth_data):
    for tooth_data in teeth_data:
        x = [tooth_data[0]]
        y = [tooth_data[1]]
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        plt.show()

        print(x)




script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../01_DATA/Z19/cutCAD_2D_Z19.txt")
gear_data = np.loadtxt(file_path)
visualize(gear_data)

num_teeth = 19

teeth_data = isolate_teeth(gear_data, num_teeth)





plt.xlabel('X')
plt.ylabel('Y')
plt.title('Isolated Teeth')
plt.show()