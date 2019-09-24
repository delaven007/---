"""
随机数
"""
import numpy as np

#命中率0.3,投10次，进几个
# n=np.random.binomial(10,0.3,1)
# n=np.random.binomial(10,0.3,99999999)
# for i in range(0,11):
# # p5=(n==5).sum()/99999999
#     p5=(n==i).sum()/99999999
#     print(i,':',p5)

#某人打客服电话，客服接通率是0.6，一共打了3次，都没人接的概率
# n=np.random.binomial(3,0.6,99999999)
# for i in range(0,4):
# # p5=(n==5).sum()/99999999
#     p=(n==i).sum()/99999999
#     print(i,':',p)

#超几何分布
# n=np.random.hypergeometric(7,3,5,10)
# print(n)
for i in range(2,6):
    n = np.random.hypergeometric(6, 4, 5, 200000)
    p=(n==i).sum()/200000
    print(i,":",p)





