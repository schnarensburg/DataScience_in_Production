import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Datei mit Zahnrad-Daten (.xyz) einlesen
def read_gear_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = []
        for line in lines:
            if line.strip():  # Leere Zeilen überspringen
                x, y, z = line.strip().split()
                points.append([float(x), float(y), float(z)])
    return np.array(points)

# Zahnrad visualisieren
def plot_gear(gear_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(gear_points[:, 0], gear_points[:, 1], gear_points[:, 2], c='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Zahnrad vermessen
def measure_gear(gear_points):
    # Beispiel für Messungen: Durchmesser, Zähnezahl usw.
    # Fügen Sie hier Ihre eigenen Messungen hinzu, je nach Bedarf.
    diameter = np.max(gear_points[:, 0]) - np.min(gear_points[:, 0])
    tooth_count = 19  # Beispielwert, bitte anpassen

    print("Durchmesser: ", diameter)
    print("Zähnezahl: ", tooth_count)

# Hauptprogramm
file_path = '/01_DATA/Z19/PointClouds/.xyz/+04.xyz'
gear_points = read_gear_data(file_path)
plot_gear(gear_points)
measure_gear(gear_points)
