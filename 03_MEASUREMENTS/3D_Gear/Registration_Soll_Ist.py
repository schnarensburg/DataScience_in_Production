import numpy as np
import open3d as o3d

def load_point_cloud(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z = line.split()
            points.append([float(x), float(y), float(z)])
    return np.array(points)

# Lade die Punktewolken
point_cloud1 = load_point_cloud('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/Z19 neu.xyz')
point_cloud2 = load_point_cloud('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+01.xyz')

#Skalierung von Ist Model(Alicona skalierung *1000)
point_cloud2 = point_cloud2 * 1000
# Erstelle Open3D-Punktewolkenobjekte
pcd1 = o3d.geometry.PointCloud()
pcd2 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector(point_cloud1)
pcd2.points = o3d.utility.Vector3dVector(point_cloud2)

# Färbe die Punktwolken
pcd1.paint_uniform_color([1, 0, 0])  # Punktewolke 1 in Rot einfärben
pcd2.paint_uniform_color([0, 1, 0])  # Punktewolke 2 in Grün einfärben

# Führe die ICP-Registrierung durch
reg_p2p = o3d.pipelines.registration.TransformationEstimationPointToPoint()
reg_result = o3d.pipelines.registration.registration_icp(pcd1, pcd2, 0.1, np.identity(4),
                                                        reg_p2p,
                                                        o3d.pipelines.registration.ICPConvergenceCriteria(
                                                            max_iteration=200))
# Hole die transformierte Punktewolke
transformed_pcd = pcd2.transform(reg_result.transformation)

# Erstelle ein Visualizer-Objekt
vis = o3d.visualization.Visualizer()
vis.create_window()

# Füge die Punktewolken zum Visualizer hinzu
vis.add_geometry(pcd1)
vis.add_geometry(transformed_pcd)

# Rendere die Punktewolken
vis.run()
vis.destroy_window()