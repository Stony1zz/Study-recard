import numpy as np
import  matplotlib.pyplot as plt



#写在前面橙色曲线为真实函数曲线
#蓝色曲线为拟合曲线




f=lambda x1:(x1-2)*(x1-6)+4
x=[2,3,4,5]
y=[4,1,0,1]
N=4
X = np.zeros([3 * (N-1) - 1, 3 * (N-1) - 1])
Y = np.zeros([3 * (N-1) - 1, 1])
w=[]
print(len(x))
def quadratic_spline(x,y):
        N=4
        X = np.zeros([3 * (N - 1) - 1, 3 * (N - 1) - 1])
        Y = np.zeros([3 * (N - 1) - 1, 1])
        N = len(x)
        j = 0
        for i in range(N-2):
            Y[2 * i] = y[i + 1]
            Y[i * 2 + 1] = y[i + 1]
            for o in range(1):
                if(i==0):
                    X[i,0]=x[i+1]
                    X[i,1]=1
                    X[2 * i + o + 1, 3 * j + 2] = x[i + 1] ** 2
                    X[2 * i + o + 1, 3 * j + 3] = x[i + 1]
                    X[2 * i + o + 1, 3 * j + 4] = 1
                    o=2
                    pass
                else:
                    X[2 * i + o, 3 * j + 2] = x[i + 1] ** 2
                    X[2 * i + o, 3 * j + 3] = x[i + 1]
                    X[2 * i + o, 3 * j + 4] = 1
                    X[2 * i + 1, 3 * j + 5] = x[i + 1] ** 2
                    X[2 * i + 1, 3 * j + 6] = x[i + 1]
                    X[2 * i + 1, 3 * j + 7] = 1
            pass
        j = 2 * (N - 1) - 2
        X[j, 0] = x[0]
        X[j, 1] = 1
        Y[j] = y[0]

        X[j + 1, -3] = x[-1] ** 2
        X[j + 1, -2] = x[-1]
        X[j + 1, -1] = 1
        Y[j + 1] = y[-1]
        j=0
        X[6, 3 * j + 0] = 1
        X[6, 3 * j + 2] = -x[1] * 2
        X[6, 3 * j + 3] = -1
        j = 0
        h = 7
        X[h, 3 * j + 2] = x[2] * 2
        X[h, 3 * j + 3] = 1
        X[h, 3 * j + 4] = 0
        X[h, 3 * j + 5] = -x[2] * 2
        X[h, 3 * j + 6] = -1
        X = np.mat(X)
        Y=np.mat(Y)
        a0=0
        w=X.I*Y
        an=0
        return w


def pre(xx):
        a0=0
        if xx<=3:
            print('111')
            return a0 * xx ** 2 + w[0] * xx + w[1]
        elif xx<=4:
            print('222')
            return w[2] * xx ** 2 + w[3] * xx + w[4]
        else:
            print('333')
            return w[5] * xx ** 2 + w[6] * xx + w[7]
w=[]

plt.figure(figsize=(8,4))
w=quadratic_spline(x,y)
xx=np.arange(2,5.1,0.1)
print(xx.size)
#调用三次样条函数
yy=np.zeros([31])
for i in range(31):
    yy[i]=pre(xx[i])
yy= np.ravel(yy,order='C')
print(yy)
print(xx)
xx=np.arange(2,5+0.1,0.1)
#调用三次样条函数
plt.plot(xx,yy)
plt.plot(xx,f(xx))
plt.show()