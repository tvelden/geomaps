import csv, sys
import time
import re
import math
from pylab import *

denom=0
filename=sys.argv[1]
fi=open(filename,'rb')
reader=csv.reader(fi)

outer_dict=dict()

for row in reader:
    temp=row[8].split(',')
    list_country=list()
    year=row[4].split(' ')
    yearf=year[len(year)-1]
    yearf=yearf.strip()
    #print yearf
    for t in temp:
        t=t.lower()
        t=t.strip()
        list_country.append(t)

    list_country=list(set(list_country))

    if len(list_country)>1:
        outer_count=0
        for w1 in list_country:
            inner_count=0
            for w2 in list_country:
                if inner_count>outer_count:
                    if outer_dict.has_key(yearf):
                        inner=outer_dict[yearf]
                        flag3=0
                        for k,v in inner.iteritems():
                            tm=k.split(',')
                            if str(w1) in tm and str(w2) in tm:
                                inner[k]+=1
                                flag3=1

                        if flag3==0:
                            co=str(w1)+','+str(w2)
                            inner[co]=1
                            outer_dict[yearf]=inner
            
                    else:
                        dictt=dict()
                        co=str(w1)+','+str(w2)
                        dictt[co]=1
                        outer_dict[yearf]=dictt
                    
                inner_count+=1
                
            outer_count+=1
            
        
yearj=1991
dictg=dict()
f2=sys.argv[2]
#print outer_dict[str(1992)]
for z in range(0,20):
    summ=0
    innerd=outer_dict[str(yearj)]
    denom=0
    for k1,v1 in innerd.iteritems():
        denom+=v1
    #print denom    
    for k,v in innerd.iteritems():
        cou=k.split(',')
        f2i=open(f2,'rb')
        reader=csv.reader(f2i)
        #print cou[0]
        for row in reader:
            if str(row[0])==str(cou[0]):
                lat1=float(row[1])
                lon1=float(row[2])
            if str(row[0])==str(cou[1]):
                lat2=float(row[1])
                lon2=float(row[2])
        f2i.close()
        pij=float(v)
        R=6371
        dlat=float(math.radians(lat2-lat1))
        dlon=float(math.radians(lon2-lon1))
        a=float((math.sin(dlat/2)*math.sin(dlat/2))+(math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)*math.sin(dlon/2)))
        c=float(2*math.atan2(math.sqrt(a),math.sqrt(1-a)))
        d=R*c
        #print d
        summ=summ+((float(pij)/float(denom))*float(d))


    dictg[yearj]=summ
    yearj+=1


index=list()
years=list()
for x in range(1991,2011):
    index.append(dictg[x])
    years.append(x)

ylim([0,8000])
xlabel("Years")
ylabel("C values")
plot(years,index)

show()
