import bpy
import numpy as np

def get_bone_head_tail_coords(scene, cam, obj, bone_name):
	R = np.array(obj.matrix_world.to_3x3())
	t = np.array(obj.matrix_world.translation)
	
	head_local_loc = obj.data.bones[bone_name].head_local
	tail_local_loc = obj.data.bones[bone_name].tail_local

	head_loc = np.dot(R,head_local_loc) + t
	tail_loc = np.dot(R,tail_local_loc) + t

	head_vec = Vector(head_loc)
	tail_vec = Vector(tail_loc)

	head_2d_loc = world_to_camera_view(scene, cam, head_vec)
	tail_2d_loc = world_to_camera_view(scene, cam, tail_vec)

	return {"head": head_2d_loc, "tail": tail_2d_loc}