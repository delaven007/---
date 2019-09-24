import numpy as np



ary=np.arange(10)
print(ary)
print(ary.clip(min=4,max=8))

print(ary.compress(ary%5==0))












