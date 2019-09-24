import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc
import scipy.integrate as si

def f(x):
    return 2 * x ** 2 + 3 * x + 4

a, b = -5, 5
x = np.linspace(a, b, 1000)
y = f(x)

mp.figure('积分', facecolor='lightgray')
mp.title('Integral', fontsize=16)
# mp.grid(linestyle='--')
mp.plot(x, y, color='orange', linewidth=6, label='f(x)', zorder=3)

# 计算f(x)在[-5,5]区间的定积分
n = 2000
x = np.linspace(a, b, n + 1)
y = f(x)
area = 0
for i in range(n):
    area += (y[i] + y[i + 1]) * (x[1] - x[0]) / 2
print(area)

n = 50
x2 = np.linspace(a, b, n + 1)
y2 = f(x2)
area = 0
for i in range(n):
    area += (y2[i] + y2[i + 1]) * (x2[i + 1] - x2[i]) / 2
print(area)
for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [x2[i], 0], [x2[i], y2[i]],
        [x2[i + 1], y2[i + 1]], [x2[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',alpha=0.5))
    
# 利用quad求积分 给出函数f，积分下限与积分上限[a, b]   返回(积分值，最大误差)
area = si.quad(f, a, b)[0]
print(area)

mp.legend()
mp.show()
