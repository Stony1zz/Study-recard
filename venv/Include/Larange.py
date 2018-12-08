import matplotlib.pyplot as plt
x = [1, 3, 5, 11]
y = [3, 15, 35, 143]
#红点是实际点
#黑线是实际曲线
#蓝色虚线是拟合曲线


#函数的系数确定
def PofLagrange(data_x, data_y, size):
    parameters = []
    # i用来控制参数的个数
    i = 0;
    while i < size:
        # j用来控制循环的变量做累乘
        j = 0;
        temp = 1;
        while j < size:
            if (i != j):
                temp *= data_x[i] - data_x[j]
            j += 1;
        parameters.append(data_y[i] / temp)
        i += 1;
    return parameters
#插值的结果返回
def CofLarange(data_x, parameters, x):
    returnValue = 0
    i = 0;
    while i < len(parameters):
        temp = 1
        j = 0;
        while j < len(parameters):
            if (i != j):
                temp *= x - data_x[j]
            j += 1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue
def Draw(data_x, data_y, new_data_x, new_data_y):
    plt.plot(new_data_x, new_data_y, 'b--')
    plt.scatter(data_x, data_y,color="red")
    plt.show()
parameters = PofLagrange(x, y, 4)
datax = [0.5,2,4,5,6,7,8,12]
datay = []
xn=[i for i in range(0,12,2)]
fn=[i**2+2*i for i in xn]
plt.plot(xn, fn, 'black')
for temp in datax:
    datay.append(CofLarange(x, parameters, temp))
x.append(5.5)
y.append(CofLarange(x, parameters, 5.5))
Draw(x, y, datax, datay)
#红点是实际点
#黑线是实际曲线
#蓝色虚线是拟合曲线