import matplotlib.pyplot as plt
import numpy as np
a=float(input("定值起始点："))
print("起始点：",a)
f=lambda x:x
f1=lambda x:x**2-2*x
f2=lambda x:2*x-2
f3=lambda x:((-f1(x))/f2(x))+x
b=[]
c=[]
def newton(x0,fun,fun2,fun3):
    b.append(0)
    c.append(x0)
    i=0
    while True:
        i=i+1
        xl=x0
        x=fun(x0)
        c.append(x0)
        b.append(fun(x0))
        c.append(fun3(x0))
        b.append(0)
        x0=fun3(x0)
        i=i+1
        if abs((x0-xl)/x0)<0.0005:
                return x0
    pass
print(newton(a,f1,f2,f3))
fig,ax = plt.subplots(figsize = (8,5) , dpi = 80)
x=np.linspace(0,10,100)
y=x**2-2*x
ax.plot(c , b)
plt.plot([0,10], [0, 0], "b--")
ax.plot(x,y,label="$x$",color="red")
ax.plot(newton(a,f1,f2,f3),f1(newton(a,f1,f2,f3)),'.')

plt.legend()
plt.show()
