import numpy as np
import matplotlib.pyplot as mp

a = np.random.randint(1, 100, 20)
b = np.random.randint(1, 100, 20)
# 均值
ave_a = np.mean(a)
ave_b = np.mean(b)
# 离差
dov_a = a - ave_a
dov_b = b - ave_b
# 协方差
cov_ab = np.mean(dov_a * dov_b)
cov_ba = np.mean(dov_b * dov_a)

print("a数组:%s,b数组:%s" % (a, b))
print("a样本方差：", np.sum(dov_a ** 2) / len(dov_a) - 1, "b样本方差:", np.sum(dov_b ** 2) / len(dov_b) - 1)
print("a与b协方差:", cov_ab, cov_ba)

# 绘图
mp.figure("协方差", facecolor='lightgray')
mp.title("a与b", fontsize=14)
mp.xlabel("x", fontsize=12)
mp.ylabel("y", fontsize=12)
x = np.arange(0, 10)
# a,b线
mp.plot(x, a, color='red', label='a')
mp.plot(x, b, color='green', label='b')
# 均线
mp.plot((0, 9), [ave_a, ave_a], linestyle='--', linewidth='12', label='a均线', alpha=0.7)
mp.plot((0, 9), [ave_b, ave_b], linestyle='--', linewidth='12', label='b均线', alpha=0.7)

mp.legend()
mp.tight_layout()
mp.show()
