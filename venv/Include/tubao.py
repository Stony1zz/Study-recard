import numpy as np
import random
import math
import matplotlib.pyplot as plt
b=[random.randint(1,101) for i in range(20)]#x
c=[random.randint(1,101) for i in range(20)]#y
m=[]
l=[]
print(b)
print(c)
i=0
while i<20:
    j=0
    while j<20:
        if (i == j):
            j = j + 1
            pass
        a=c[j]-c[i]
        b=b[i]-b[j]
        c=b[i]*c[j]-c[i]*b[j]
        sign1=0
        sign2=0
        k=0
        while k<=20:
            if(k==i|k==j):
                pass
            if(a*b[k]+b*c[k]-c)<=0:
                sign1=sign1-1
            if(a*b[k]+b*c[k]-c)>=0:
                sign2=sign2+1
        if(sign1==2-i|sign2==2-i):
            m.append(i)
            m.append(j)
            l.append(i)
            l.append(j)
        j=j+1
        pass
    pass
