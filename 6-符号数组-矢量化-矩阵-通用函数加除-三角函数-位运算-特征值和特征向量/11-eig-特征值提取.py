"""11-eig-特征值提取"""

import numpy as np

A=np.mat('1,3,6;2,4,8;7,2,9')
print(A)

#提取特征值和特征向量
eigvals,eigvecs=np.linalg.eig(A)
print(eigvals,eigvecs)

#逆向推导原矩阵
M=eigvecs*np.diag(eigvals)*eigvecs.I
print(M)

#抹掉部分特征值，生成原矩阵
eigvals[2:]=0
M_=eigvecs*np.diag(eigvals)*eigvecs.I
print(M_)









