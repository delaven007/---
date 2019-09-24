"""
奇异值分解
"""
import numpy as np

M=np.mat('1 6 9; 5 7 2 ')
print(M)
U,sv,V=np.linalg.svd(M,full_matrices=False)     #是否结果为完全方阵
print(U,U.shape)
print(sv,sv.shape)
print(V,V.shape)

#生成原矩阵
#改变值
sv[1]=0
print(type(U),type(V))
M2=U *np.diag(sv)*V
print(M2)




