import pickle

class Athletelist(list):
     def __init__(self,a_name,a_bir=None,a_times=[]):
          list.__init__([])
          self.name=a_name
          self.bir=a_bir
          self.extend(a_times)

     def top3(self):
          return(sorted(set([sanitize(t) for t in self]))[0:3])

def sanitize(time_string):
     if '-' in time_string:
          splitter='-'
     elif ':' in time_string:
          splitter=':'
     else:
          return(time_string)
     (min,sec)=time_string.split(splitter)
     return(min+'.'+sec)


def get_coach_score(file_str):
     try:
          with open(file_str) as ff:
               data=ff.readline()
               lod=data.strip().split(',')
               return(Athletelist(lod.pop(0),lod.pop(0),lod))
     except IOError as ioerr:
          print('IOErroe'+str(ioerr))
          return(None)

def put_to_store(file_list):
     all_athlete={}
     for each_file in file_list:
          ath=get_coach_score(each_file)
          all_athlete[ath.name]=ath
          
     try:
          with open('athlete.pickle','wb') as athfile:
               pickle.dump(all_athlete,file=athfile)
     except IOError as ioerr:
          print('IOError:'+str(ioerr))
     return(all_athlete)

def get_from_store():
     all_athlete=dict()
     try:
          with open('athlete.pickle','rb') as athfile:
               all_athlete=pickle.load(athfile)
     except IOError as ioerr:
          print('IOError:'+str(ioerr))
     return(all_athlete)
     
