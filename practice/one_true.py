'''
甲、乙、丙三个人在一起做作业，有一道数学题比较难，当他们三个人都把自己的解法
说出来以后，甲说：“我做错了。”乙说：“甲做对了。”丙说：“我做错了。”在一旁的丁
看到他们的答案并听了她们的意见后说：“你们三个人中有一个人做对了，有一个人说对
了。”请问，他们三人中到底谁做对了?
'''

def one_true(li):
    true_sum=0
    for i in li:
        if i==1:
            true_sum+=1
    return true_sum==1

def tell_one_true(li):
    tell_true_sum=0
    for i in enumerate(li):
        if i==(0,0):
            tell_true_sum+=1
        if i==(0,1):
            tell_true_sum+=1
        if i==(2,0):
            tell_true_sum+=1
    return tell_true_sum==1

def main():
    list_0_1=[0,1]
    all_case=[[x1,x2,x3] for x1 in list_0_1 for x2 in list_0_1 for x3 in list_0_1]
    all_case=list(filter(one_true,all_case))
    all_case=list(filter(tell_one_true,all_case))
    print(all_case)

if __name__ == '__main__':
    main()