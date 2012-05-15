import sys
import csv
filename=open(sys.argv[1],'rb')

fo=open(sys.argv[2],'wb')
csvWriter = csv.writer( fo )
cities=str()
countries=str()
flag=0
row_number=0
for line in filename.readlines():
    temp=line.split(' ')
    if str(temp[0])=='ID':
        flag=0
        flag1=0
        flag2=0

    if str(temp[0])=='CT':
        if flag1==1:
            cities=cities+','
        temp1=temp[1].split('\n')
        cities=cities+str(temp1[0])
        flag1=1

    if str(temp[0])=='CO':
        if flag2==1:
            countries=countries+','
        temp1=temp[1].split('\n')
        countries=countries+str(temp1[0])
        flag2=1

    if str(temp[0])=='RF' and flag==0:
        row_number+=1
        #print cities
        city_country=list()
        city_country.append(cities)
        #print city_country
        city_country.append(countries)
        csvWriter.writerow(city_country)
        cities=str()
        countries=str()
        flag=1
    


   
