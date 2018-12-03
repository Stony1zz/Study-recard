import matplotlib.pyplot as plt
import numpy as np
a,b=map(float,input("输入区间：").split())
print("你输入的区间：",a,b)
f=lambda x:x**2-4
f2=lambda x:x**0.5-1

def shiwei(x0,x1,fun):
    xr=x1-fun(x1)*(x0-x1)/(fun(x0)-fun(x1))
    while True:
        if fun(x0)*fun(xr)<0:
            x0=xr
        elif fun(x1)*fun(xr)<0:
            x1=xr
        else:
            return xr
        last_xr=xr
        xr=x1-fun(x1)*(x0-x1)/(fun(x0)-fun(x1))
        if abs((xr-last_xr)/xr)<0.0000005:
                return xr
    pass
plt.figure(figsize=(8,4))
x=np.linspace(a,b,100)
y=x**2-4
z=x**0.5-1
x1=shiwei(a,b,f)
y1=x1**2-4
x2=shiwei(a,b,f2)
z1=x2**0.5-1
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$x**2-4$",color="red")
plt.plot(x,z,"b--",label="$x**0.5-1$")
plt.plot(x1,y1,'ro')
plt.plot(x2,z1,'bo')
plt.title("试位法")
plt.legend()
plt.show()
print(shiwei(a,b,f))

print(shiwei(a,b,f2))