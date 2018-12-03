# -*- coding: utf-8 -*
import numpy as np
import matplotlib.pyplot as plt
def Least_squares(x, y):
    x_ = x.mean()
    y_ = y.mean()
    m = 0
    n = 0
    k = 0
    q = 0
    for i in np.arange(30):
        k = (x[i] - x_) * (y[i] - y_)
        m += k
        q = np.square(x[i] - x_)
        n = n + q
        a = m / n
        b = y_ - a * x_
    return a, b
x = np.linspace(0, 30, num=30)
y = 0.2*x+[np.random.random() for _ in range(30)]
a, b = Least_squares(x, y)
print(a, b)
y1 = a * x + b
plt.figure(figsize=(6, 4), facecolor='w')
plt.plot(x, y, 'b.')
plt.plot(x, y1, 'r-')
plt.show()