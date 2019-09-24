import matplotlib.pyplot as ma
x=[]
y=[]
ma.ion()
for i in range(1000):
    x.append(i)
    y.append(i*2)
    ma.clf()
    ma.plot(x,y)
    ma.pause(1)
    ma.ioff()
