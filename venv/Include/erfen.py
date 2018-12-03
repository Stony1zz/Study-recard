import matplotlib.pyplot as plt
import numpy as np
a,b=map(float,input("输入区间：").split())
print("你输入的区间：",a,b)
f=lambda x:x**2-4
f2=lambda x:x**0.5-1

def two_mid(head,end,fun):
    print(type(head),type(end))
    mid=(head+end)/2
    while True:
        if fun(mid)*fun(head)<0:
            end=mid
        elif fun(mid)*fun(head)>0:
            head=mid
        else:
            return mid
        last_mid=mid
        mid=(head+end)/2
        if abs((mid-last_mid)/mid)<0.000005:
                return mid
    pass

plt.figure(figsize=(8,4))
x=np.linspace(a,b,100)
y=x**2-4
z=x**0.5-1
x1=two_mid(a,b,f)
y1=x1**2-4
x2=two_mid(a,b,f2)
z1=x2**0.5-1
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$x**2-4$",color="red")
plt.plot(x,z,"b--",label="$x**0.5-1$")
plt.plot(x1,y1,'ro')
plt.plot(x2,z1,'bo')
plt.title("二分法")
plt.legend()
plt.show()
print(two_mid(a,b,f))

print(two_mid(a,b,f2))