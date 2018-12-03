import numpy as np
import matplotlib.pyplot as plt
print('f(x)=x^5-3.5*x^4+2.75*x^3+2.125*x^2-3.875*x+1.25的根，使用初始估计r=s=-1')
i = 0
f=lambda x:x**5-3.5*x**4+2.75*x**3+2.125*x**2-3.875*x-1.25
a = [1.25,-3.875,2.125,2.75,-3.5,1]
b = [0,0,0,0,0,0]
c = [0,0,0,0,0,0]
rs=[-1,-1,0,0]
rs_0 = [0,0]
n = 5
x = [0,0,0,0,0]
n_0=[3,1]
w = 0
j = 0
count = 0
def beer(r,s):
    global n,w,j,count
    count = count+1
    global i
    #B
    i = 3
    b[5] = a[5]  # bn = an
    b[4] = a[4] + r * b[5]
    while i != -1:
        b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
        i = i - 1
    #C
    i = 3
    c[5] = b[5]
    c[4] = b[4] + r * c[5]
    while i != -1:
        c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        i = i - 1
    r = (b[0] * c[3] - b[1] * c[2]) / (c[2] * c[2] - c[1] * c[3]) + rs[0]
    s = (b[0] * c[2] - b[1] * c[1]) / (c[3] * c[1] - c[2] * c[2]) + rs[1]
    rs[2] = r
    rs[3] = s
    #误差分析
    rs_0[0] = (rs[2] - rs[0]) / rs[2]
    rs_0[1] = (rs[3] - rs[1]) / rs[3]
    rs[0] = rs[2]
    rs[1] = rs[3]
    if (abs(rs_0[0])<0.00005)|(abs(rs_0[1])<0.00005): #误差满足条件
        print(count,'次迭代得')
        x[j] = (rs[2]+(rs[2]**2+4*rs[3])**(1/2))/2  # 4
        print('x',j,'=',x[j])
        j = j + 1
        x[j] = (rs[2]-(rs[2]**2+4*rs[3])**(1/2))/2  # 3
        print('x',j,'=',x[j])
        j =j+1
        n = n_0[w]
        w=w+1
        if n == 1:
            x[4] =(-rs[2]) / rs[3]
            print('x', 4, '=', x[4])
            print('全部根:',x)
        elif (n > 2):
            count = 0
            a[0] =b[2]
            a[1] = b[3]
            a[2] = b[4]
            a[3] = b[5]
            a[4] = 0
            a[5] = 0
            beer(rs[2], rs[3])
    else:
        beer(rs[2],rs[3])
beer(-1,-1)
plt.figure()
x_range=np.linspace(-3, 5, 100)
plt.plot(x_range,f(x_range),'g')
plt.hlines(0,plt.xlim()[0],plt.xlim()[1])
plt.scatter([x[0],x[1],x[4]],[0,0,0])
plt.show()
