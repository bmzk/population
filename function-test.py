import copy 
import math 
import random
import os
import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
from matplotlib import animation

MaxAge=150

def f1(x1,a=1.005):
    return (1.05**(x1-MaxAge))*200
def f2(x2):
    return 10*5*(math.cos(0.01*(x2+70)*math.pi)+1)
def dead(x0):
    '''返回'''
    return f1(x0)+f2(x0)*0.1
year=1
y0=[]
y1=[]
y2=[]
for i in range(MaxAge):
    y0.append(0)
    y1.append(random.random())
    y2.append(0)

def display():
    global year
    for i in range(MaxAge):
        y1[i]=f1(i )
        y2[i]=f2(i+year)
        y0[i]=dead(i)
    year+=1

xlist=np.linspace(1,MaxAge,MaxAge)
fig, ax = plt.subplots()

# line, 表示只取返回值中的第一个元素
l0, = ax.plot(xlist,y0,linestyle = '--')
l1, = ax.plot(xlist,y1 )
l2, = ax.plot(xlist,y2)#,linestyle = '--')

# 定义动画的更新
def update(i):
    display()
    plt.xlabel(u'第 ' +str(year)+'年',fontproperties='SimHei',fontsize=14)
    plt.ylim(0,100)#max(per)*1.03)
    l0.set_ydata(y0)
    l1.set_ydata(y1)
    l2.set_ydata(y2)
    #return l1,

# 创建动画
ani = animation.FuncAnimation(fig = fig, func = update,  interval = 100)#, blit = False)
# 展示动画
plt.show()
