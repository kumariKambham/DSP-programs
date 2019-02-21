import matplotlib.pyplot as plt
import numpy as np

sample = 1000
f=100
Fs=800
n=np.arange(sample)
x=np.sin(2*np.pi*n*f/Fs)
f=10
Fs=200
y=np.sin(2*np.pi*n*f/Fs)
z=x+y
plt.subplot(311)
plt.plot(n,x)
plt.subplot(312)
plt.plot(n,y)
plt.subplot(313)
plt.plot(n,z)


plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

