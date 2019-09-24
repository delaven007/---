
import numpy as np
a=np.array([1,-2,2,-2,6])
b=np.array([3,3,-4,-8,6])

print(np.bitwise_xor(a,b))
print(a ^ b)

c=a^b
r=np.where(c<0)[0]      #返回符合条件的索引数组
print(r)

a=np.arange(1000000)
print(a[a&(a-1)==0])

j=a&(a-1)
for i in range(1000000):
    if a[j==0]:
        print(i)








