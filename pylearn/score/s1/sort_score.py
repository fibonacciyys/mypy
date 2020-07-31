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
               return(lod)
     except IOError as ioerr:
          print('IOErroe'+str(ioerr))

def unique(alist):
     uni_alist=[]
     for each_item in alist:
          if each_item not in uni_alist:
               uni_alist.append(each_item)
     return(uni_alist)

try:
     """with open('james.txt') as jaf:data=jaf.readline()
     james=data.strip().split(',')
     with open('julie.txt') as juf:data=juf.readline()
     julie=data.strip().split(',')
     with open('mikey.txt') as mif:data=mif.readline()
     mikey=data.strip().split(',')
     with open('sarah.txt') as saf:data=saf.readline()
     sarah=data.strip().split(',')"""

     james=get_coach_score('james.txt')
     julie=get_coach_score('julie.txt')
     mikey=get_coach_score('mikey.txt')
     sarah=get_coach_score('sarah.txt')
     
     """sa_james=[]
     sa_julie=[]
     sa_mikey=[]
     sa_sarah=[]

     for each_t in james:
          sa_james.append(sanitize(each_t))
     for each_t in julie:
          sa_julie.append(sanitize(each_t))
     for each_t in mikey:
          sa_mikey.append(sanitize(each_t))
     for each_t in sarah:
          sa_sarah.append(sanitize(each_t))

     print(sorted(sa_james))
     print(sorted(sa_julie))
     print(sorted(sa_mikey))
     print(sorted(sa_sarah))"""

     
     james=sorted(set([sanitize(t) for t in james]))[0:3]
     julie=sorted(set([sanitize(t) for t in julie]))[0:3]
     mikey=sorted(set([sanitize(t) for t in mikey]))[0:3]
     sarah=sorted(set([sanitize(t) for t in sarah]))[0:3]

     print(james)
     print(julie)
     print(mikey)
     print(sarah)


except IOError as err:
     print('IOError'+str(err))
