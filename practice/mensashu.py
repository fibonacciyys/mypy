
def norepeated(li):
    return len(list(set(li)))==4

def main():
    put_in=['+','-','*','/']
    all_case=[[x1,x2,x3,x4] for x1 in put_in for x2 in put_in for x3 in put_in for x4 in put_in]
    all_case_list=list(filter(norepeated,all_case))
    list_0_1=[0,1]
    is_add_brackets=[[x1,x2,x3,x4] for x1 in list_0_1 for x2 in list_0_1 for x3 in list_0_1 for x4 in list_0_1]
    is_add_brackets_list=list(is_add_brackets)
    #print(all_case_list)
    for lis in all_case_list:
        for i in is_add_brackets_list:
            s='({}'
            for  x,item in enumerate(lis):
                if i[x]:
                    item1=')'+item+'('
                else:
                    item1=item
                if x==3:
                    s=s+item1+'{})'
                else:
                    s=s+item1+'{}'
            s=s.format(2,3,4,5,6)
            #print(s)
            if eval(s)==10:
                print(s,'=10')


if __name__ == '__main__':
    main()