"""12-lily：图像特征值提取"""

import numpy as np
import scipy.misc  as sm
import matplotlib.image as mi
import matplotlib.pyplot as mp
import imageio
#读取图片数据 True:提取亮度矩阵
img=mi.imread('/home/tarena/1904/数据分析/data/da_data/lily.jpg')
print(img.shape)

#提取特征值
eigvals,eigvecs=np.linalg.eig(np.mat(img))
#逆向推导原矩阵
eigvals[250:]=0
img2=eigvecs*np.diag(eigvals)*eigvecs.I



#绘制图片
mp.figure('lily',facecolor='lightgray')
mp.subplot(121)
mp.imshow(img,camp='gray')
mp.xticks([])
mp.yticks([])
mp.subplot(122,camp='gray')
mp.imshow(img2.real)
mp.xticks([])
mp.yticks([])

#奇异值分解
U,sv,V=np.linalg.svd(np.mat(img))               #转成矩阵格式
sv[50:]=0                   #只保留50
print(type(U),type(V))
img3=U*np.diag(sv)*V
print(img3)
mp.subplot(121)
mp.imshow(img3.real,camp='gray')
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()
















