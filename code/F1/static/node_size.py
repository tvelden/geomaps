import csv, sys
from collections import *
from numpy import *
filename = 'file'

fi=open(sys.argv[2],'wb')
        
flag=0
count1=list()
dict1=dict()
csvWriter=csv.writer(fi)
lineheader=['ID','CT','CO','lat','lon','CNT']
csvWriter.writerow(lineheader)
lat=list()
appeared_lat=list()
appeared_city_same_id=list()
with open(sys.argv[1], 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       #print row[2]
       flag12=0
       for temp1 in appeared_city_same_id:
           if temp1[0]==row[0]:
               if temp1[1]==row[3]:
                   flag12=1
                   break
       if flag12==0:
          lat.append(row[3])
       temp=list()
       temp.append(row[0])
       temp.append(row[3])
       appeared_city_same_id.append(temp)

       

cnt=Counter()
print len(lat)
for word in lat:
    cnt[word]+=1


with open(sys.argv[1], 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       temp=list()
       temp=row
       temp.append(log(cnt[row[3]])+1)
       csvWriter.writerow(row)
    


      
    



