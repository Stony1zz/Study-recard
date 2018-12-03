# -*- coding: utf-8 -*-
import turtle
import random
import time

f = open('point.txt', 'w')
for i in range(100):
    x = random.randrange(-250, 250, 10)
    y = random.randrange(-200, 200, 10)
    f.write(str(x) + ',' + str(y) + '\n')
f.close()
point = []

f = open('point.txt')
for i in f:
    try:
        temp = i.split(',')
        x = float(temp[0]);
        y = float(temp[1])
        point.append((x, y))
    except:
        print
        'a err'
f.close()

point = list(set(point))  # 去除重复的点

n = 0
for i in range(len(point)):
    if point[n][1] > point[i][1]:
        n = i

p0 = point[n]
point.pop(n)


def compare(a, b):
    x = [a[0] - p0[0], a[1] - p0[1]]
    y = [b[0] - p0[0], b[1] - p0[1]]
    dx = (x[0] ** 2 + x[1] ** 2) ** 0.5
    dy = (y[0] ** 2 + y[1] ** 2) ** 0.5
    cosa = x[0] / dx
    cosb = y[0] / dy
    if cosa < cosb:
        return 1
    elif cosa > cosb:
        return -1
    else:
        if dx < dy:
            return -1
        elif dx > dy:
            return 1
        else:
            return 0


point.sort(compare)
point.insert(0, p0)
ep = point[:]  # 复制元素，操作ep不会对point产生影响
tag = 0
while tag == 0:
    tag = 1
    l = len(ep)
    for i in range(l):
        i1, i2, i3 = (i, (i + 1) % l, (i + 2) % l)
        x, y, z = (ep[i1], ep[i2], ep[i3])
        a1, a2 = ((y[0] - x[0], y[1] - x[1]), (z[0] - y[0], z[1] - y[1]))
        if a1[0] * a2[1] - a1[1] * a2[0] < 0:
            tag = 0
            ep.pop(i2)
            break
        elif a1[0] * a2[1] - a1[1] * a2[0] == 0 and a1[0] * a2[0] < 0:
            # ==0应改写,360度的情况
            tag = 0
            ep.pop(i2)
            break


def drawpoint(point, color, line):
    p = turtle.getturtle()
    p.hideturtle()
    turtle.delay(1)
    if (line == 'p'):
        p.speed(0)
        for i in point:
            p.pu()
            p.color(color)
            p.goto(i)
            p.pd()
            p.dot()
    elif (line == 'l'):
        p.pu()
        p.speed(1)
        for i in point:
            p.color(color)
            p.goto(i)
            p.pd()
            p.dot()
        p.goto(point[0])


drawpoint(point, 'black', 'p')
drawpoint(ep, 'red', 'l')
time.sleep(1)
