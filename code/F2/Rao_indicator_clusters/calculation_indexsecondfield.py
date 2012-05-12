import csv, sys
import re
import math
from pylab import *
names = ['first_cluster','second_cluster','third_cluster','fourth_cluster','fifth_cluster','sixth_cluster','seventh_cluster','eighth_cluster','ninth_cluster','tenth_cluster','eleventh_cluster']
cluster=0
for name in names:
    filename=sys.argv[1] + "\\" + name + "\\filecitiescount"
    print filename
    year=1991
    dict1=dict()
    for t in range(0,20):
        count_of_documents=0
        with open(filename+str(year)+".csv",'rb') as f:
            reader=csv.reader(f)
            final_scanned_cities=list()
            for row in reader:
                row[0]=str(row[0]).strip()
                if str(row[0]) not in final_scanned_cities:
                    final_scanned_cities.append(str(row[0]))
                    count_of_documents+=1
        f.close()
        with open(filename+str(year)+".csv",'rb') as f:
            reader1=csv.reader(f)
            list_of_cities=list()
            for row in reader1:
                temp=list()
                pi=float(float(row[5])/float(count_of_documents))
                lat=row[3]
                lon=row[4]
                temp.append(lat)
                temp.append(lon)
                temp.append(pi)
                if temp not in list_of_cities:
                    list_of_cities.append(temp)

        counti=0
        #print list_of_cities
        #haversine formula
        summ=0.0
        for city in list_of_cities:
            lat1=float(city[0])
            lon1=float(city[1])
            pi=float(city[2])
            countj=0
            for city2 in list_of_cities:
                if countj>counti:
                    lat2=float(city2[0])
                    lon2=float(city2[1])
                    pj=float(city2[2])
                    R=6371
                    dlat=float(math.radians(lat2-lat1))
                    dlon=float(math.radians(lon2-lon1))
                    a=float((math.sin(dlat/2)*math.sin(dlat/2))+(math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)*math.sin(dlon/2)))
                    c=float(2*math.atan2(math.sqrt(a),math.sqrt(1-a)))
                    d=R*c
                    #print d
                    summ=summ+(float(pi)*float(pj)*float(d))
                    

                countj+=1
            counti+=1    

                        
        dict1[year]=summ
        year+=1
    #print dict1
    index=list()
    years=list()
    path = sys.argv[2]
    with open(path+'\\'+str(cluster)+".csv",'wb') as fw:
        print path+str(cluster)+".csv"
        cluster+=1

        fw.write('CNT')
        fw.write('\n')
        for x in range(1991,2011):
            fw.write(str(dict1[x]))
            fw.write('\n')


    
