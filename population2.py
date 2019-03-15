import turtle
import copy 
import math 
import random
import os
import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
from matplotlib import animation

MaxAge=120
StartBornAge=18
EndBornAge=35
BornChance=0.001*80  #2018年人口出生率降至10.94‰
deadPercent=lambda x:0.0*math.cos(0.01*(x+20)*math.pi)+1.0004**x-1#0.01*1.5 #通常用千分数,2016年，我国人口死亡率为7.09‰
year=1
pop=[]
for i in range(MaxAge):
    pop.append(int(random.random()*10000))
bornPop=copy.deepcopy(pop)
DeadPop=copy.deepcopy(pop)



def Sub_BornAndDead():
    '''
    根据当前各年龄人口计算出生人口和死亡人口
    '''
    for i in range(MaxAge):
        DeadPop[i]=int(pop[i]*deadPercent(i))+i
        if pop[i]<=DeadPop[i]:
            DeadPop[i]=pop[i]
        bornPop[i]=0
        if i>=StartBornAge:
            if  i<=EndBornAge:
                bornPop[i]=int(pop[i]*BornChance)
def f_str(*mystring,n=8):
    ''' 格式化输出字符串,n为输出长度 ,str(s).center(n)'''
    v=""
    for i in mystring:
        if type(i)==int:
            v=v+'{:,}'.format( i ).rjust(n)  
        else:  
            v=v+str(i).center(n)
    return v
def print_f(*mystring,m=10):
    print(f_str(*mystring,n=m))

def count():
    '''计算各年龄段人口
    '''
    for i in range(1,MaxAge):
        pop[MaxAge-i-1]=pop[MaxAge-i-1]-DeadPop[MaxAge-i-1]
        pop[MaxAge-i]=pop[MaxAge-i-1]
    pop[0]=sum(bornPop)

def display():
    os.system("cls")
    Sub_BornAndDead()
    global year
    print('year:',year,'    TotalPop:','{:,}'.format( sum(pop) ))
    print_f('born:',sum(bornPop),'','bornPer:','{:.3%}'.format(sum(bornPop)/sum(pop)),m=12)
    print_f('Dead:',sum(DeadPop),'','DeadPer:','{:.3%}'.format(sum(DeadPop)/sum(pop)),m=12)
    print_f('Old:',sum(DeadPop[60:]),"",' OldPer:','{:.3%}'.format(sum(DeadPop[60:])/sum(pop)),m=12)
    print_f('VeryOld:',sum(DeadPop[80:]),'','VeryOld:','{:.3%}'.format(sum(DeadPop[80:])/sum(pop)),m=12)
    #line=20
    #for i in range(0,line):
        #print_f(i,pop[i],i,pop[i+line],i+line*2,pop[i+line*2],i+line*3,pop[i+line*3],i+line*4,pop[i+line*4],m=12)
    count ()
    year+=1
    

X=np.linspace(1,MaxAge,MaxAge)

fig, ax = plt.subplots()

# line, 表示只取返回值中的第一个元素
line, = ax.plot(X, pop)

# 定义动画的更新
def update(i):
    display()
    plt.xlabel(u'第 ' +str(year)+' 年  总人口: '+'{:,}'.format(sum(pop)),fontproperties='SimHei',fontsize=14)
    plt.ylim((0, max(pop)*1.03))
    line.set_ydata(pop)
    return line,

# 定义动画的初始值
def init():
    display()
    line.set_ydata(pop)
    return line,

# 创建动画
ani = animation.FuncAnimation(fig = fig, func = update, 
 interval = 200, blit = False)
# 展示动画
plt.show()
