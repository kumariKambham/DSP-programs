import numpy as np
import matplotlib.pyplot as plt
p=int(input("enter the order of moving average system"))
Fs=20000
f1=50
f2=5000
y=np.zeros(1000)
t=np.linspace(0,4000,1000)
u=np.sin(2*np.pi*f1*t/Fs)
v=np.sin(2*np.pi*f2*t/Fs)
x=u+v
sum=0
q=p-1
for i in range(0,1000,1):
	for k in range(0,q,1):
		sum=sum+x[i-k]
	y[i]=float((sum)/(p))
	sum=0
print(y)
plt.subplot(411)
plt.plot(t,u)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()
