import plot3D_module as plot3d


# initialize with big box size
my_3d = plot3d.ThreeD_plot(100, 100, 100)
my_3d.add_box_another((0.0, 0.0, 0.0),(77.0, 87.0, 48.0))
# if the box is overlap with the other, print(Unavailable: position{}, xyz_length{})
my_3d.show()