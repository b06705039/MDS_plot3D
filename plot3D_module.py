from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import count
plt.style.use('seaborn')



class ThreeD_plot:
    def __init__(self, x_size, y_size, z_size):
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')

        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size

        self.ax.set_xlim(0, x_size)
        self.ax.set_ylim(y_size,0)
        self.ax.set_zlim(0, z_size)
        self.ax.set_xlabel('Y axis')
        self.ax.set_ylabel('X axis')
        self.ax.set_zlabel('Z axis')
        
        self.index = count()
        self.box_df = pd.DataFrame(columns=['box_id','x_range','y_range','z_range','color'])

    
        
    def add_box_another(self, position, length):
        y_range, x_range, z_range = zip(position,[position[i]+length[i] for i in range(3)])
        
        # check if available to add
        range_list = np.concatenate((x_range, y_range, z_range),axis=None)
        for i in range(2):
            for j in range(len(self.box_df)):
                for range_i in range(len(range_list)):
                    range_column = int(range_i/2)+1
                    if(range_list[range_i]>float(self.box_df.iloc[j,range_column][0]) \
                       and range_list[range_i]<float(self.box_df.iloc[j,range_column][1])):
                        print("Unavailable: start posision_{}, xyz_length_{}".format(position,length))
                        return None
        
        # start to add box
        color = np.random.rand(3,)

        xx, yy, zz = np.meshgrid(x_range, y_range, z_range)
        self.ax.plot_wireframe(xx[0], yy[0], zz[0], color=color)
        self.ax.plot_wireframe(xx[1], yy[1], zz[1], color=color)
        self.ax.plot_surface(xx[0], yy[0], zz[0], color=color, alpha=0.2)
        self.ax.plot_surface(xx[1], yy[1], zz[1], color=color, alpha=0.2)

        xx, zz, yy = np.meshgrid(x_range, z_range, y_range)
        self.ax.plot_wireframe(xx[0], yy[0], zz[0], color=color)
        self.ax.plot_wireframe(xx[1], yy[1], zz[1], color=color)
        self.ax.plot_surface(xx[0], yy[0], zz[0], color=color, alpha=0.2)
        self.ax.plot_surface(xx[1], yy[1], zz[1], color=color, alpha=0.2)

        zz, yy, xx = np.meshgrid(z_range, y_range, x_range)
        self.ax.plot_wireframe(xx[0], yy[0], zz[0], color=color)
        self.ax.plot_wireframe(xx[1], yy[1], zz[1], color=color)
        self.ax.plot_surface(xx[0], yy[0], zz[0], color=color, alpha=0.2)
        self.ax.plot_surface(xx[1], yy[1], zz[1], color=color, alpha=0.2)
        
        new_s = {'box_id':self.index, 'x_range':x_range,'y_range':y_range,'z_range':z_range,'color':color}
        self.box_df = self.box_df.append(new_s, ignore_index=True)
        
        
        
    def show(self):
        
        plt.show()





# initialize with big box size
# my_3d = ThreeD_plot(100, 100, 100)
# my_3d.add_box_another((-1,-1,-0.5),(1,2,1))
# my_3d.add_box_another((0,-1,0), (1,2,0.5))
# my_3d.add_box_another((0,-1,-0.5), (1,2,1))
# my_3d.show()