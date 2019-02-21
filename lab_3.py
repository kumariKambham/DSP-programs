import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('name.wav')
#fs1,data1=wav.read('kumar.wav')
#fs=np.float(2*fs)
#fs1=np.float(fs1)
#print(fs,len(data),data)
#t=np.arange(0,len(data)/fs,1/fs)
#t1=np.arange(0,len(data1)/fs1,1/fs1)
#a1=plt.subplot(211)
plt.plot(data)
#a2=plt.subplot(212)
#plt.plot(t1,data1)
plt.show()
wav.write('song.wav',(4*fs),data)
