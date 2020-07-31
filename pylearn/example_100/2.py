# -*- coding: utf-8 -*-

i=int(input('请输入的你当月利润:'))
profit=[1000000,600000,400000,200000,100000,0]
bonus=[0.01,0.015,0.03,0.05,0.075,0.1]
sum_bouns=0
for x in range(6):
    if i>profit[x] :
        sum_bouns+=(i-profit[x])*bonus[x]
        i=profit[x]
        
print('bonus:'+str(sum_bouns))