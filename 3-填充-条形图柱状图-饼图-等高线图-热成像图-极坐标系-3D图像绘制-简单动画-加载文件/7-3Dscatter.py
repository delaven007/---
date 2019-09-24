"""
3D散点图
"""

import numpy as np
import matplotlib.pyplot as mp
from  mpl_toolkits.mplot3d import axes3d
n=300
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
z=np.random.normal(0,1,n)

mp.figure('3D Points',facecolor='lightgray')
ax3d=mp.gca(projection='3d')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
# ax3d.scatter(x,y,z,s=70,alpha=0.6,color='orange')
d=x**2+y**2+z**2
ax3d.scatter(x,y,z,s=70,alpha=0.6,c=d,cmap='jet')
mp.tight_layout()
mp.show()


