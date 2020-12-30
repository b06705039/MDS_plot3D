import plot3D


# initialize with big box size
my_3d = ThreeD_plot(100, 100, 100)
my_3d.add_box_another((-1,-1,-0.5),(1,2,1))
# if the box is overlap with the other, print(Unavailable: position{}, xyz_length{})
my_3d.add_box_another((0,-1,0), (1,2,0.5))
my_3d.add_box_another((0,-1,-0.5), (1,2,1))
my_3d.show()