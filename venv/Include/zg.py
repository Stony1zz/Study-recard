import matplotlib.pyplot as plt
import numpy as np
a,d=map(float,input("输入起始俩点：").split())
print("你输入的点：",a,d)
f=lambda x:x**2-2*x
f2=lambda x:x**0.5-1

def secant(x0,x1,fun):
    fig, ax = plt.subplots(figsize=(8, 5), dpi=80)
    x = np.linspace(0, 10, 100)
    y = x ** 2 - 2 * x
    ax.plot(x, y, label="$x$", color="red")
    plt.plot([0,10], [0, 0], "--")
    i=0;
    while True:
        ax.plot([x1,x1],[0,fun(x1)] )

        x = x0 - (fun(x0) * (x1 - x0) /((fun(x1) - fun(x0))))
        ax.plot([x1, x0, x], [fun(x1),fun(x0),0])
        if abs((x0 - x) / x0) < 0.000005:
            ax.plot(x,fun(x),'.')
            return x
        x1 = x0
        x0=x
    pass
print(secant(a,d,f))



plt.legend()
plt.show()
