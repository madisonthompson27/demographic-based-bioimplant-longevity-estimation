"""
Main housing for program, will contain elements of GUI and blender graphics.
Uses open3d for point alignment and meshes. 
"""

#imports
import numpy as np
import open3d as o3d


# creating a point cloud
point_cloud = o3d.data.PCDPointCloud()
pcd = o3d.io.read_point_cloud("femur.xyz")

#o3d.open3d.visualization.draw_geometries([pcd]) #test line for visualization


# voxel downsampling to create a uniform and basic point cloud
downpcd = pcd.voxel_down_sample(voxel_size = 0.05)

#o3d.open3d.visualization.draw_geometries([downpcd]) #testing voxel distribution

# estimating normal vectors
downpcd.estimate_normals(search_param = o3d.geometry.KDTreeSearchParamHybrid(radius = 0.1, max_nn = 30))

#o3d.open3d.visualization.draw_geometries([downpcd], point_show_normal=True) #testing vectors, they are uniform


# creating an alpha shape
distances = downpcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist

bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(downpcd, o3d.utility.DoubleVector([radius, radius * 2]))

#print(np.asarray(mesh.vertices))
#print(np.asarray(mesh.triangles))


# visualizing the mesh 
o3d.open3d.visualization.draw_geometries([downpcd])
o3d.open3d.visualization.draw_geometries([bpa_mesh])