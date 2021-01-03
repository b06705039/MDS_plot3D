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
        
        self.index = 0
        self.box_df = pd.DataFrame(columns=['box_id','position','length','color'])

    
        
    
    def add_box_another(self, position, length):
        position = np.array(list(position))
        length = np.array(list(length))
        
        if(self.checkIfOverlap(position, length)):
            return
    
        y_range, x_range, z_range = zip(position,[position[i]+length[i] for i in range(3)])
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
        
        new_s = {'box_id':self.index, 'position':position, 'length':length, 'color':color}
        self.box_df = self.box_df.append(new_s, ignore_index=True)
        
        self.index += 1
        
    def checkIfOverlap(self, position, length):
        y_position = position
        y_length = length
        for box_i in range(len(self.box_df)):
            
            x_position = self.box_df.iloc[box_i,1]
            x_length = self.box_df.iloc[box_i,2]
        
            proj_y0 = y_position - x_position - x_length
            proj_y1 = y_position + y_length - x_position - x_length

            for axis in [[1,0,0],[0,1,0],[0,0,1]]:
                x_vec = x_length * np.array(axis)
                proj = self.project(proj_y0,x_vec) * self.project(proj_y1,x_vec)
                if(proj>1):
                    return 0
                elif(axis == [0,0,1]):
                    print('<overlap> x: {}, y: {} in {}'.format([x_position,x_length],[y_position,y_length],axis))
                    return 1

        
    def project(self, y, x):
        return np.dot(y, x)/np.sqrt(sum((x)**2)) **2
        
        
    def show(self):
        
        plt.show()





# initialize with big box size
# my_3d = ThreeD_plot(100, 100, 100)
# my_3d.add_box_another((-1,-1,-0.5),(1,2,1))
# my_3d.add_box_another((0,-1,0), (1,2,0.5))
# my_3d.add_box_another((0,-1,-0.5), (1,2,1))
# my_3d.show()