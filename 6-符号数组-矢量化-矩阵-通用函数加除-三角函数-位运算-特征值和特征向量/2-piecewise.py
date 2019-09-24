import numpy as np
import matplotlib.pyplot as mp

ary=np.array([60,50,70,32,65,28,73,93])
r=np.piecewise(ary,[np.all([ary<=100,ary>=60],axis=0),ary<60],[1,0])
print(r)