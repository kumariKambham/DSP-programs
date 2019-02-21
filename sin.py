import matplotlib.pyplot as plt
import numpy as np
fs=2500
f1=200
n=50
x=np.arange(n)
a=np.sin(2*np.pi*f1/fs*x)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

plt.show()
