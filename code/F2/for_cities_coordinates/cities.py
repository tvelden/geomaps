import sys
import csv
import re
from googlemaps import GoogleMaps
gmaps=GoogleMaps(api_key='')

import time
fo=open(sys.argv[2],'wb')
csvWriter = csv.writer( fo )  #Defaults to the excel dialect
i=0
import csv, sys
filename = sys.argv[1]
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            countries=list()
            i=i+1
            if i>0:
                print i
                countries=row[1].split(',')
                cities=list()
                cities=row[0].split(',')
                #print row[0]
                if row[0]:
                    #print "great"
                    country_count=0
                    for city in cities:
                        time.sleep(0.5)
                        address=str(city)+','+str(countries[country_count])
                        #print address
                        try:
                            lat, lng=gmaps.address_to_latlng(address)
                        except:
                            address=str(countries[country_count])
                            lat, lng=gmaps.address_to_latlng(address)
                            
                        lat_list=list()
                        lat_list.append(i)
                        lat_list.append(str(city))
                        lat_list.append(str(countries[country_count]))
                        lat_list.append(lat)
                        lat_list.append(lng)
                        csvWriter.writerow(lat_list)
                        country_count+=1
                        address=str()
                    
                
    except csv.Error, e:
        i=i+1
        print i
        exit
