
import numpy as np

# name=np.array(['apple','orange','banana','pipe','juice'])
# price=[200,1500,700,900,6000]
# volume=np.array([80,100,90,80,550])
#
# #联合间接排序
# sort_indx=np.lexsort((-volume,price))
# print(name[sort_indx])

#
a=np.array([3,5,6,8])
b=np.array([6,3])
indics=np.searchsorted(a,b)
print(indics)
d=np.insert(a,indics,b)
print(d)























