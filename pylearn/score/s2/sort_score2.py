def sanitize(time_string):
     if '-' in time_string:
          splitter='-'
     elif ':' in time_string:
          splitter=':'
     else:
          return(time_string)
     (min,sec)=time_string.split(splitter)
     return(min+'.'+sec)

class Athlete:
     def __init__(self,a_name,a_bir=None,a_times=[]):
          self.name=a_name
          self.bir=a_bir
          self.times=a_times

     def top3(self):
          return(sorted(set([sanitize(t) for t in self.times]))[0:3])

     def add_time(self,time_value):
          if isinstance(time_value,str):
               self.times.append(time_value)
          elif isinstance(time_value,list):
               self.times.extend(time_value)

class Athletelist(list):
     def __init__(self,a_name,a_bir=None,a_times=[]):
          list.__init__([])
          self.name=a_name
          self.bir=a_bir
          self.extend(a_times)

     def top3(self):
          return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_score(file_str):
     try:
          with open(file_str) as ff:
               data=ff.readline()
               lod=data.strip().split(',')
               #return({'name':lod.pop(0),'bir':lod.pop(0),'times':str(sorted(set([sanitize(t) for t in lod]))[0:3])})
               #return(Athlete(lod.pop(0),lod.pop(0),lod))
               return(Athletelist(lod.pop(0),lod.pop(0),lod))
     except IOError as ioerr:
          print('IOErroe'+str(ioerr))
          return(None)
def main():
     james=get_coach_score('james2.txt')
     #print(james['name']+"'s fastest times are:"+james['times'])
     #print(james.name+"'s fastest times are:"+str(james.top3()))
     print(james.name+"'s fastest times are:"+str(james.top3()))

if __name__=='__main__':
     main()
