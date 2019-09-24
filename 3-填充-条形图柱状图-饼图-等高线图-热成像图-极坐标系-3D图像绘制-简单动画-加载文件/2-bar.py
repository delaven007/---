"""柱状图"""

import numpy as np
import matplotlib.pyplot as mp

apples=np.array([15,5,46,45,56,54,4,32,7,98,54,54])
oranges=np.array([64,45,71,65,6,84,65,49,6,84,6,5])

mp.figure('Bar Chart',facecolor='lightgray')
mp.title('Bar Chart',fontsize=16)
mp.xlabel('Date',fontsize=16)
mp.ylabel('Volume',fontsize=16)
mp.grid(linestyle=':',axis='x')
x=np.arange(apples.size)
# bottom=np.zeros(12)
# bottom[2]=20
mp.bar(x-0.2,oranges,0.4,color='orangered',label='Orange')
mp.bar(x+0.2,apples,0.4,color='dodgerblue',label='Apple')

mp.xticks(x,['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()




