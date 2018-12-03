import numpy as np
import random
import math
import matplotlib.pyplot as plt
b=[random.randint(1,101) for i in range(50)]
c=[random.randint(1,101) for i in range(50)]
print(b)
print(c)
e=10000
i=0
j=0
while i<50:
    while j<50:
        if(i==j):
            j=j+1
            pass
        else:
            m=math.sqrt(abs(((b[i])-b[j])**2)+abs(((c[i])-c[j])**2))
            if m<e:
                a=[i,j]
                d=[i,j]
                e=m
            j=j+1
            pass
    i=i+1
    j=0
    pass
print('最近对是：')
print('[',b[a[0]],',',c[d[0]],']')
print('[',b[a[1]],',',c[d[1]],']')
fig,ax = plt.subplots(figsize = (8,5) , dpi = 80)
x=np.linspace(0,10,100)
plt.plot(b, c, ".")
plt.plot([b[a[0]],b[a[1]]],[c[d[0]],c[d[1]]],'r--')
plt.legend()
plt.show()