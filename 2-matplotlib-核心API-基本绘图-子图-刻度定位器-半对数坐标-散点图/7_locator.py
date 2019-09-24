#刻度线

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.figure as mg

locators=['mp.NullLocator()',
         'mp.MaxNLocator(nbins=4)',
         'mp.AutoLocator()',
         'mp.FixedLocator([2.5,5,7.5,10])']

mp.figure('Locator',facecolor='gold')
for i ,locator in enumerate(locators):
    mp.subplot(len(locators),1,i+1)
    ax=mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    mp.xlim(0,10)
    mp.ylim(-1,1)
    mp.yticks([])
    ax.spines['bottom'].set_position(('data',0))
    #设置刻度定位器
    maj_loc=eval(locator)        #每隔1一个刻度
    ax.xaxis.set_major_locator(maj_loc)

    min_loc=mp.MultipleLocator(0.1)        #每隔0.1一个刻度
    ax.xaxis.set_minor_locator(min_loc)

    # max_loc=mp.MaxNLocator(nbins=4)        #每隔0.1一个刻度
    # ax.xaxis.set_major_locator(max_loc)




mp.tight_layout()
mp.show()
















