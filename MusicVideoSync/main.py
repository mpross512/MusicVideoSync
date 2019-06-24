import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import wave

np.set_printoptions(threshold=np.inf)

#sound = wave.open('440.wav', "rb")
#print(sound.getnframes())
#print(sound.readframes(100))


rate, data = wav.read('sample_new.wav')
print("RAW DATA")
#print(data[:rate])
#print("Sampling")
print("Length of data", len(data))
fft_out = np.fft.fft(data, rate)
freqs = np.fft.fftfreq(len(fft_out))

#plt.plot(data)
print("Rate", rate)
#plt.plot(np.abs(fft_out))
#plt.rcParams['agg.path.chunksize'] = 10000
#plt.xlim(100, 18000)
#plt.minorticks_on()
#plt.show()
print("FFT OUT")
print(freqs.min(), freqs.max())
print("Length of fft_out", len(fft_out), "\nLength of freqs", len(freqs))
idx = np.argmax(np.abs(fft_out))
freq = freqs[idx]
print("Freq", freq)
print(freq * rate)
