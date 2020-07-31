import os

import pickle
import movies

man=[]
other=[]
if os.path.exists('sketch.txt') :     
     with open('sketch.txt') as data:

          for each_line in data:
               try:
                    (role,line_spoken)=each_line.split(':',1)
                    """print(role,end='')
                    print(' said:',end='')
                    print(line_spoken,end='')"""
                    line_spoken=line_spoken.strip()
                    if role=='Man':
                         man.append(line_spoken)
                    elif role == 'Other Man':
                         other.append(line_spoken)
               except ValueError:
                    pass
          print()


else:
     print('the data file is missing')

try:
     with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
          pickle.dump(man,man_file)
          pickle.dump(other,other_file)

except pickle.PickleError as perr:
     print('pickle erroe'+str(perr))

except IOError as err :
     print('file error'+str(err))

#140
