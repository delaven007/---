"""合成方波"""
import numpy as np
import matplotlib.pyplot as mp

x=np.linspace(-2*np.pi,2*np.pi,1000)
y1=4*np.pi*np.sin(x)

y2=4*np.pi/3*np.sin(3*x)
y3=3*np.pi/5*np.sin(5*x)

y=np.zeros(x.size)
for i in range(1,1000):
    y+=4*np.pi/(2*i-1)*np.sin((2*i-1)*x)
mp.plot(x,y1,label='sinx')
mp.plot(x,y2,label='sin3x')
mp.plot(x,y3,label='sin5x')
mp.plot(x,y,label=r'$y$')
mp.legend()
mp.show()
































