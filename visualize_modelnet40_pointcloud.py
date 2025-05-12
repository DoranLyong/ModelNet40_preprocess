import pickle
import numpy as np
import open3d as o3d
import os

# --- Load ModelNet40 .dat file ---
dat_path = "./data/modelnet40_test_8192pts_fps.dat"

with open(dat_path, "rb") as f:
    dataset = pickle.load(f)

pointclouds = np.array(dataset[0])    # (N, 8192, 6); 6:= (x,y,z,R,G,B)
labels = np.array(dataset[1])       # (N,)

# --- Optionally load class names ---
shape_name_path = "./data/modelnet40_shape_names.txt"
shape_names = []
if os.path.exists(shape_name_path):
    with open(shape_name_path, "r") as f:
        shape_names = [line.strip() for line in f.readlines()]

# --- Choose sample index to visualize ---
index = 0
points = pointclouds[index]     # shape: (8192, 6)
label = labels[index].item()
label_name = shape_names[label] if shape_names else f"Class {label}"

# --- Separate coordinates and RGB ---
xyz = points[:, :3].astype(np.float64)
rgb = points[:, 3:6].astype(np.float64)

# Normalize RGB from [-1, 1] → [0, 1]
rgb = (rgb + 1.0) / 2.0
rgb = np.clip(rgb, 0.0, 1.0)

# --- Create Open3D point cloud object ---
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
pcd.colors = o3d.utility.Vector3dVector(rgb)

# --- Visualize (GUI window) ---
print(f"🔍 Visualizing sample index {index} - Class: {label_name}")
o3d.visualization.draw_geometries(
    [pcd],
    window_name=f"ModelNet40: {label_name}",
    width=800,
    height=600,
    zoom=0.6,
    front=[0, 0, -1],
    lookat=[0, 0, 0],
    up=[0, -1, 0]
)
