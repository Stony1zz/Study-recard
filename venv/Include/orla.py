import numpy as np
from matplotlib.pyplot import plot,savefig
import matplotlib.pyplot  as plt
r=2
K=3
h=0.001
step=5000
u=np.zeros((1,step+1))
x=np.zeros((1,step+1))
u[0,0]=0.5
for i in range(0,step):
    u[0,i+1]=u[0,i]+h*(r*u[0,i]-u[0,i]*u[0,i]*r/K)
    x[0,i]=h*i
print(x[0,step-1],u[0,step])
plt.xlim(0,5)
plt.ylim(0,3.5)
plt.xlabel("x")
plt.ylabel("u")
plt.plot(x,u,'--*b')
plt.show()
