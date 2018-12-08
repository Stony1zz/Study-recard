import numpy as np
import matplotlib.pyplot as plt
#递归
def getdif(xi,fi):
    if len(xi)> 2 and len(fi) > 2:
        return (getdif(xi[:len(xi) - 1],fi[:len(fi) -1]) - getdif(xi[1:len(xi)],fi[1:len(fi)]))/float(xi[0] -xi[-1])
    return (fi[0] - fi[1])/float(xi[0]-xi[1])
#求w，使用闭包函数
def get_w(i,xi):
    def wi(x):
        result = 1.0
        for j in range(i):
           result *= (x - xi[j])
        return result
    return wi
def get_Newton(xi,fi):
    def Newton(x):
        result = fi[0]
        for i in range(2,len(xi)):
           result += (getdif(xi[:i],fi[:i])* get_w(i-1,xi)(x))
        return result
    return Newton
xn=[i for i in range(-20,22,2)]
fn=[i** 2 for i in xn]

Nx = get_Newton(xn,fn)


temp_x=[i for i in range(-20,22)]
temp_y=[Nx(i) for i in temp_x]


plt.figure(figsize=(6, 4), facecolor='w')
plt.plot(temp_x, temp_y, 'b-')
plt.plot(xn, fn, 'r.')
plt.show()