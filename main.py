import CSF
import open3d as o3d
import numpy as np

# read and set point cloud
pc = o3d.io.read_point_cloud('./test.pcd')
csf = CSF.CSF()
csf.setPointCloud(pc.points)

# parameter settings. More details about parameter: http://ramm.bnu.edu.cn/projects/CSF/download/
csf.params.bSloopSmooth = False
csf.params.cloth_resolution = 0.5

# filtering
ground = CSF.VecInt() 
non_ground = CSF.VecInt()
csf.do_filtering(ground, non_ground)

# saving ground point cloud
pc_ground = o3d.geometry.PointCloud()
pc_ground.points = o3d.utility.Vector3dVector(np.asarray(pc.points)[ground])
pc_ground.colors = o3d.utility.Vector3dVector(np.asarray(pc.colors)[ground])
o3d.io.write_point_cloud("./ground.pcd", pc_ground)

# saving non-ground point cloud
pc_non_ground = o3d.geometry.PointCloud()
pc_non_ground.points = o3d.utility.Vector3dVector(np.asarray(pc.points)[non_ground])
pc_non_ground.colors = o3d.utility.Vector3dVector(np.asarray(pc.colors)[non_ground])
o3d.io.write_point_cloud("./non_ground.pcd", pc_non_ground)

# o3d.visualization.draw_geometries([pc_ground, pc_non_ground])




