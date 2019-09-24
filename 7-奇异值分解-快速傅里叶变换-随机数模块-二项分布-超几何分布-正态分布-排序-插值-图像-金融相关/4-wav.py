import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, noised_sigs = wf.read('../data/da_data/noised.wav')
# print("sample_rate:", sample_rate)
# print("noised_sigs:", noised_sigs, "noised_sigs.shape:", noised_sigs.shape)

noised_sigs = noised_sigs / 2 ** 15
times = np.arange(len(noised_sigs)) / sample_rate
# print("times:", times)
mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)  # 画子图
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=20)
# mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178], c='orangered', label='Noised')  # 取前178个元素
mp.legend()
mp.tight_layout()

# 绘制频域图
# comp_ary = nf.fft(noised_sigs)
# print(comp_ary)
freqs = nf.fftfreq(times.size, 1 / sample_rate)
noised_ffts = nf.fft(noised_sigs)
# print("noised_ffts:",noised_ffts)
noised_pows = np.abs(noised_ffts)
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
#半对数坐标.semilogy
mp.semilogy(freqs[freqs >= 0], noised_pows[freqs >= 0], c='limegreen', label='Noised')
mp.legend()

# 在频谱中去除噪声
maxpow_freq = freqs[noised_pows.argmax()]       #找到噪声的下标
# print("maxpow_freq:",maxpow_freq)
# 噪声下标
noised_indas = np.where(freqs != maxpow_freq)
# print("noised_indas:",noised_indas)
noised_ffts=noised_ffts.copy()
# 噪声数据全抹为零
noised_ffts[noised_indas] = 0                   #噪声能量抹为零
filter_pows=np.abs(noised_ffts)
# 绘制降噪之后的频谱图
pows = np.abs(noised_ffts)
mp.subplot(224)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='limegreen', label='Noised')

# 逆向傅里叶变换，输出时域函数图像
filter_sigs = nf.ifft(noised_ffts).real
mp.subplot(223)  # 画子图
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=20)
# mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178], c='blue', label='Filter')

# 保存文件
wf.write('../data/da_data/filter.wav', sample_rate, (filter_sigs * 2 ** 15).astype(np.int16))

mp.tight_layout()
mp.show()
