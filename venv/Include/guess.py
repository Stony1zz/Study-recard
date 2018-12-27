import numpy as np
max = [[2, 3, 4, 18], [4, 5, 6, 30], [7, 9, 12, 64]]
def guess(max):
    i = 0;
    j = 0;
    length= len(max)
    while j < length - 1:
        line = max[j]
        temp = line[j]
        templete = []
        for x in line:
            x = x / temp
            templete.append(x)
        max[j] = templete
        flag = j + 1
        while flag < length:
            templete1 = []
            temp1 = max[flag][j]
            i = 0
            for x1 in max[flag]:
                if x1 != 0:
                    x1 = x1 - (temp1 * templete[i])
                    templete1.append(x1)
                else:
                    templete1.append(0)
                i += 1
            max[flag] = templete1
            flag += 1
        j += 1
    return max
print("高斯消去前：")
for i in range(len(max)):
        print(max[i])
results = guess(max)
print("高斯消去后：")
for i in range(len(max)):
        print(max[i])
