# First import the library
import pyrealsense2 as rs
import numpy as np
from matplotlib import pyplot as plt

# explicit function to normalize array
def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    matrix = matrix*255
    return matrix

# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()

try:

    # Create a pipeline object. This object configures the streaming camera and owns it's handle
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    depth_data = depth.as_frame().get_data()
    
    np_image = np.asanyarray(depth_data)
    print(np_image)

    np_image = normalize_2d(np_image)
    
    plt.imshow(np_image, interpolation='nearest', cmap='Greys')
    plt.show()

    # save numpy array 
    np.save("test.npy", np_image)
       
finally:
    pipeline.stop()
