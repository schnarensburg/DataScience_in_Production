import numpy as np
import open3d as o3d
import trimesh


def load_point_cloud(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z = line.split()
            points.append([float(x), float(y), float(z)])
    return np.array(points)

# Lade die Punktewolken
point_cloud1 = load_point_cloud('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+01.xyz')
point_cloud2 = load_point_cloud('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+02.xyz')




# Erstelle Open3D-Punktewolkenobjekte
pcd1 = o3d.geometry.PointCloud()
pcd2 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector(point_cloud1)
pcd2.points = o3d.utility.Vector3dVector(point_cloud2)

# Färbe die Punktwolken
pcd1.paint_uniform_color([1, 0, 0])  # Punktewolke 1 in Rot einfärben
pcd2.paint_uniform_color([0, 1, 0])  # Punktewolke 2 in Grün einfärben

# Schätze Normale für die Punktwolken
pcd1.estimate_normals()
pcd2.estimate_normals()

# Führe die ICP-Registrierung durch
reg_p2p = o3d.pipelines.registration.TransformationEstimationPointToPoint()
reg_result = o3d.pipelines.registration.registration_icp(pcd1, pcd2, 0.1, np.identity(4),
                                                        reg_p2p,
                                                        o3d.pipelines.registration.ICPConvergenceCriteria(
                                                            max_iteration=200))
# Hole die transformierte Punktewolke
transformed_pcd = pcd2.transform(reg_result.transformation)

# Skaliere die Punktwolken auf die gleiche Größe
pcd1.scale(1 / np.max(pcd1.get_max_bound() - pcd1.get_min_bound()), center=pcd1.get_center())
transformed_pcd.scale(1 / np.max(transformed_pcd.get_max_bound() - transformed_pcd.get_min_bound()), center=transformed_pcd.get_center())

# Repariere die Dreiecksnetze
mesh1, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd1)
mesh1.remove_degenerate_triangles()
mesh1.remove_duplicated_triangles()
mesh1.remove_duplicated_vertices()
mesh1.remove_non_manifold_edges()
mesh1.remove_unreferenced_vertices()

mesh2, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(transformed_pcd)
mesh2.remove_degenerate_triangles()
mesh2.remove_duplicated_triangles()
mesh2.remove_duplicated_vertices()
mesh2.remove_non_manifold_edges()
mesh2.remove_unreferenced_vertices()

# Berechne Oberfläche der Punktewolken
surface_area1 = mesh1.get_surface_area()
surface_area2 = mesh2.get_surface_area()

# Berechne maximale Abweichungen zwischen den Punktewolken
distances = pcd1.compute_point_cloud_distance(transformed_pcd)
max_distance = np.max(distances)


# Erstelle trimesh-Objekte für die weitere Vermessung
mesh1_trimesh = trimesh.Trimesh(vertices=np.asarray(mesh1.vertices), faces=np.asarray(mesh1.triangles))
mesh2_trimesh = trimesh.Trimesh(vertices=np.asarray(mesh2.vertices), faces=np.asarray(mesh2.triangles))

# Berechne äußere Kantenlänge der Modelle mit trimesh
edge_length1 = np.sum(mesh1_trimesh.edges_unique_length)
edge_length2 = np.sum(mesh2_trimesh.edges_unique_length)

# Weitere Ausgabe der berechneten Informationen
print("Punktewolke 1:")
print("Äußere Kantenlänge:", edge_length1)
print("Oberfläche:", surface_area1)
print()
print("Punktewolke 2 (ausgerichtet):")
print("Äußere Kantenlänge:", edge_length2)
print("Oberfläche:", surface_area2)
print()
print("Maximale Abweichung zwischen den Modellen",max_distance)
# Visualisierung der Punktwolken
o3d.visualization.draw_geometries([pcd1, pcd2])