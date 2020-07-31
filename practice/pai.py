import random

def get_pai1(num):
    sum=0
    for i in range(num):
        x=random.random()
        y=random.random()
        if x**2+y**2<1:
            sum+=1
    return sum*4/num

def get_pai2(num):
    product=1
    for i in range(num):
        x=i+1
        x<<=1
        product*=x**2/((x-1)*(x+1))
    return product*2

def get_pai3(num):
    sum=0
    for i in range(num):
        x=1/(2*i+1)*(-1)**i
        sum+=x
    return sum*4

if __name__ == '__main__':
    x=1000000
    pai1,pai2,pai3=get_pai1(x),get_pai2(x),get_pai3(x)
    print(pai1,'\n'+str(pai2),'\n'+str(pai3))