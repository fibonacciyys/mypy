import sys
def print_lol(the_list,indent=False,times=1,fn=sys.stdout):
        for each_item in the_list:
                if isinstance(each_item,list):
                        
                        print_lol(each_item,indent,times+1,fn)
                else:
                        if indent:
                                for num in range(times):
                                        print("\t",end='',file=fn)
                        print(each_item,file=fn)
			
