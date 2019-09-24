"""
傅里叶变换   拆方波
"""
import numpy as np
import matplotlib.pyplot as mp
import numpy.fft as nf

x=np.linspace(-2*np.pi,2*np.pi,1000)
y=np.zeros(x.size)
for i in range(1,1000):
    y+=4*np.pi/(2*i-1)*np.sin((2*i-1)*x)
# mp.plot(x,y,label=r'$y$')

#画图
mp.figure('FFT',facecolor='orange')
mp.subplot(1,2,1)
mp.title('Time Domain',fontsize=18)
#针对方波y做fft
comp_ary=nf.fft(y)
y2=nf.ifft(comp_ary).real           #.real消除警告
mp.plot(x,y2,color='green',linewidth=5,alpha=0.5,label=r'$y$')

#绘制频域图形（频率/能量）
mp.subplot(1,2,2)
freqs=nf.fftfreq(y.size,x[1]-[0])
print(freqs)
#能量
powers=np.abs(comp_ary)         #复数的模
print(powers)
mp.title('Frequency Domain',fontsize=16)
mp.plot(freqs,powers,color='orangered',label='frequency')

# mp.grid(linestyle='-.')
mp.legend()
mp.show()
































