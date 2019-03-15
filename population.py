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
BornPop=copy.deepcopy(pop)
DeadPop=copy.deepcopy(pop)
<<<<<<< HEAD


=======
MaxAge=100
startpop=10000
StartBornAge=18
EndBornAge=35
year=1
pop[10]=startpop
>>>>>>> 817c768efb2c535e07fd9c7917bef3f61056e8f5

def Sub_BornAndDead():
    '''根据当前各年龄人口计算出生和死亡人口,即计算BornPop和DeadPop.
    内部设定参数出生率和死亡率.
    '''
<<<<<<< HEAD
    根据当前各年龄人口计算出生人口和死亡人口
    '''
=======
    BornChance=0.001*20  #2018年人口出生率降至10.94‰
    #0.01*1.5 #通常用千分数,2016年，我国人口死亡率为7.09‰
    deadPercent=lambda x:0.002*math.cos(0.01*(x+20)*math.pi)+1.001**x-1
>>>>>>> 817c768efb2c535e07fd9c7917bef3f61056e8f5
    for i in range(MaxAge):
        DeadPop[i]=int(pop[i]*deadPercent(i))+i
        if pop[i]<=DeadPop[i]:
            DeadPop[i]=pop[i]
        BornPop[i]=0
        if i>=StartBornAge:
            if  i<=EndBornAge:
<<<<<<< HEAD
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
=======
                BornPop[i]=int(pop[i]*BornChance)

def Sub_refresh_pop():
    '''更新各年龄人口,即更新pop
>>>>>>> 817c768efb2c535e07fd9c7917bef3f61056e8f5
    '''
    for i in range(1,MaxAge):
        pop[MaxAge-i-1]=pop[MaxAge-i-1]-DeadPop[MaxAge-i-1]
        pop[MaxAge-i]=pop[MaxAge-i-1]
<<<<<<< HEAD
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
=======
        #TotalPop=TotalPop+pop[MaxAge-i]
    pop[0]=sum(BornPop)

def Sub_ScreenDisplay(v_year :int=0):
    '''屏幕显示内容'''
    fs=lambda v_str,v_width=8: str(v_str).center(v_width)  #FormatString,固定宽度格式化显示字符串
    def 显示统计信息():
        #人口出生信息
        print(fs('     '),fs('Total'),fs('Growth'),fs('Born'),fs('Dead'))
        print(fs('数量',6),fs(sum(pop)),fs(sum(BornPop)-sum(DeadPop)),fs(sum(BornPop)),fs(sum(DeadPop)))
        print(fs('比例',6),fs('100%'),fs(round(100*(sum(BornPop)-sum(DeadPop))/sum(pop),2)),
        fs(round(100*sum(BornPop)/sum(pop),2)),fs(round(100*sum(DeadPop)/sum(pop),2))    )
    def 显示详细信息():
        for i in range(MaxAge):  #MaxAge
            print(fs(str(v_year)+'年',5),fs(str(i)+'岁',5),fs(pop[i]),fs(BornPop[i]),fs(DeadPop[i]))
    显示统计信息()
    显示详细信息()
##__绘图__##############################################

import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
#plt.show()
g=[0]
while len(g)<100:
    g.append(0)
yy=1

def 绘图():
    g[year-1]=round(100*(sum(BornPop)-sum(DeadPop))/sum(pop),2)
    X=np.linspace(1,100,100,endpoint=True)#0 to 100的100个值
    print('1'*22)
    plt.plot(X,g)
    print('2'*22)
    plt.show()
    pass
##__主过程__############################################
def Sub_main():
    Sub_BornAndDead()
    global year
    Sub_ScreenDisplay(year)
    print('准备绘图')
    g[year-1]=round(100*(sum(BornPop)-sum(DeadPop))/sum(pop),2)
    print('完成绘图')
    year=year+1

    Sub_refresh_pop()
    

##__程序运行语句__#####################################################################
while  year  !=-1:
    Sub_main()
    if year>49:
        绘图()
        input('input year')






>>>>>>> 817c768efb2c535e07fd9c7917bef3f61056e8f5
