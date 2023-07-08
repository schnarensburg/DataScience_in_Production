import pandas as pd
import matplotlib.pyplot as plt
import os

#Load 2dimCAD.csv
script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "../01_DATA/Z13/PointClouds/.csv2D/KW012D.csv")
df = pd.read_csv(file, header=None)

x = df.iloc[:, 0]
y = df.iloc[:, 1]

plt.scatter(x, y)
plt.xlabel('X-asis')
plt.ylabel('Y-asis')
plt.title('2D Coordinate Plot')
plt.show()