import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import matplotlib.pyplot as mp

#读取文件
original = sm.imread('../data/da_data/lily.jpg', True)
print(original.shape)

mp.figure('Ndimage',facecolor='lightgray')
mp.subplot(2,2,1)
mp.axis('off')
mp.imshow(original,cmap='gray')
# #高斯模糊
median = sn.median_filter(original, 10)
mp.subplot(2,2,2)
mp.axis('off')
mp.imshow(median,cmap='gray')
print(median)
#旋转
median1=sn.rotate(original,45)
mp.subplot(2,2,3)
mp.axis('off')
mp.imshow(median1,cmap='gray')
print(median1)
#边缘识别
prewitt=sn.prewitt(original)
mp.subplot(2,2,4)
mp.axis('off')
mp.imshow(prewitt,cmap='gray')
print(prewitt)



# #角度旋转
# rotate = sn.rotate(original, 45)
# #边缘识别
# prewitt = sn.prewitt(original)
# mp.figure('Image', facecolor='lightgray')
# mp.subplot(221)
# mp.title('Original', fontsize=16)
# mp.axis('off')
# mp.imshow(original, cmap='gray')
# mp.subplot(222)
# mp.title('Median', fontsize=16)
# mp.axis('off')
# mp.imshow(median, cmap='gray')
# mp.subplot(223)
# mp.title('Rotate', fontsize=16)
# mp.axis('off')
# mp.imshow(rotate, cmap='gray')
# mp.subplot(224)
# mp.title('Prewitt', fontsize=16)
# mp.axis('off')
# mp.imshow(prewitt, cmap='gray')
mp.tight_layout()
mp.show()