import matplotlib.pyplot as plt
import numpy as np
a=float(input("定值起始点："))
print("起始点：",a)
f=lambda x:x
f1=lambda x:(2*x)**0.5
f2=lambda x:x**0.5-1
b=[]
c=[]
def dddd(x0,fun):
    while True:
        x=fun(x0)
        c.append(x0)
        b.append(fun(x0))
        c.append(x)
        b.append(x)
        x0=fun(x)
        c.append(x)
        b.append(fun(x))
        c.append(fun(x))
        b.append(fun(x))
        if abs(x-x0)<0.0000005:
                print(b)
                return x
    pass
print(dddd(a,f1))
fig,ax = plt.subplots(figsize = (8,5) , dpi = 80)
x=np.linspace(0,10,100)
y=x
z=(2*x)**0.5
ax.plot(c , b)
ax.plot(x,y,label="$x$",color="red")
ax.plot(x,z,"b--",label="$2x**0.5$")

plt.legend()
plt.show()
