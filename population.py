import turtle
import copy 
import math 
import random
pop=[]
for i in range(100):
    pop.append(int(random.random()*10000))
bornPop=copy.deepcopy(pop)
DeadPop=copy.deepcopy(pop)
MaxAge=100
startpop=10000
StartBornAge=18
EndBornAge=35
BornChance=0.001*20  #2018年人口出生率降至10.94‰
deadPercent=lambda x:0.002*math.cos(0.01*(x+20)*math.pi)+1.0015**x-1#0.01*1.5 #通常用千分数,2016年，我国人口死亡率为7.09‰
year=1
pop[10]=startpop

def Sub_BornAndDead():
    '''
    根据当前各年龄人口
    '''
    for i in range(MaxAge):
        DeadPop[i]=int(pop[i]*deadPercent(i))+i
        if pop[i]<=DeadPop[i]:
            DeadPop[i]=pop[i]
        bornPop[i]=0
        if i>=StartBornAge:
            if  i<=EndBornAge:
                bornPop[i]=int(pop[i]*BornChance)

                


def count():
    #tqeryrythjte
    '''12124423153454
    wqtetreter
    '''
    def __doc__():

    for i in range(1,MaxAge):
        pop[MaxAge-i-1]=pop[MaxAge-i-1]-DeadPop[MaxAge-i-1]
        pop[MaxAge-i]=pop[MaxAge-i-1]
        #TotalPop=TotalPop+pop[MaxAge-i]
    pop[0]=sum(bornPop)

def display():
    BornAndDead()
    global year
    print('year:',year,'    TotalPop:',sum(pop) )
    print('born:'.center(8),str(sum(bornPop)).center(8),'bornPercent:'.center(8),(str(round(1000*sum(bornPop)/sum(pop),2))+'‰').center(8))
    print('Dead:'.center(8),str(sum(DeadPop)).center(8),'DeadPercent:'.center(8),(str(round(1000*sum(DeadPop)/sum(pop),2))+'‰').center(8))
    line=20
    for i in range(0,line):
        print(str(i).center(5),str(pop[i]).center(5),
        '    ',str(i+line).center(5),str(pop[i+line]).center(5),
        '    ',str(i+line*2).center(5),str(pop[i+line*2]).center(5),
        '    ',str(i+line*3).center(5),str(pop[i+line*3]).center(5),
        '    ',str(i+line*4).center(5),str(pop[i+line*4]).center(5))
    count ()
    year+=1
    
    #print( bornPop)


def test():
    global year
    for i in range(0,MaxAge):
        print(str(year).center(5),str(i).center(5),str(pop[i]).center(5),str(DeadPop[i]).center(5),str(bornPop[i]).center(5))
    BornAndDead()
    
    print('year:',year,'    TotalPop:',sum(pop) )
    #print('born:'.center(5),str(pop[0]).center(5),'bornPercent:'.center(5),str(100*pop[0]/sum(pop)).center(5))

    #line=20
    #for i in range(0,line):
        # print(str(i).center(5),str(pop[i]).center(5),
        # '    ',str(i+line).center(5),str(pop[i+line]).center(5),
        # '    ',str(i+line*2).center(5),str(pop[i+line*2]).center(5),
        # '    ',str(i+line*3).center(5),str(pop[i+line*3]).center(5),
        # '    ',str(i+line*4).center(5),str(pop[i+line*4]).center(5))
    count ()
    year+=1

#for j in range(199):
    
    
    #test()



while  year  !=0:
    #global year
    print('year:',year,'    TotalPop:',sum(pop) ,'00000000000000000000')
    test()
    display()
    input('input year')









def test():
    '''
    函数说明
    '''
    print('测试函数')