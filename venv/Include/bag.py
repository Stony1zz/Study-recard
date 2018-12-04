import numpy as np
#定义重量
weight=[0,0,0,0,0]
weight[0]=3
weight[1]=1
weight[2]=2
weight[3]=2
weight[4]=1
#定义价值
worth=[0,0,0,0,0]
worth[0]=10
worth[1]=3
worth[2]=9
worth[3]=5
worth[4]=6

name={}
name[0]='water'
name[1]='book'
name[2]='food'
name[3]='jacket'
name[4]='camera'
print(name)
print('重量：',weight)
print('价值',worth)
table=np.zeros((len(weight),6))
result=np.zeros((len(weight), 6), dtype=np.dtype((np.str_,500)))
#print(table)
for i in range(0,len(weight)):
    worthf = 0
    for j in range(0,6):
        #获取重量
        this_weight=weight[i]
        this_worth=worth[i]
        if(i>0):
            before_worth=table[i-1,j]
            temp=0
            #print('1',worthf,before_worth)
            if(this_weight<=j+1):
                temp=table[i-1,j-this_weight]
            if(this_weight<=j):
                worthf=this_worth+temp
            if(worthf>before_worth):
                table[i,j]=worthf
                if (temp==0):
                    result[i][j]=name[i]
                else:
                    result[i][j]=name[i] + "," + result[i - 1][j - this_weight]
            else:
                table[i,j]=before_worth
                result[i,j]=result[i-1][j]
        else:
            if(this_weight-1<=j):
                table[i][j]=this_worth
                result[i][j]=name[i]
print(table)
print('最后装载结果：',result[i][j])



