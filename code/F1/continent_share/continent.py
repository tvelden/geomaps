import csv
import re
from pylab import *
import math
import numpy as np
import matplotlib.pyplot as plt
dict_continent=dict()
dict_continent['asia']=['hong','Bangladesh'
,'Bhutan'
,'Brunei Darussalam'
,'Cambodia'
,'China'
,'Hong Kong'
,'India'
,'Indonesia'
,'Japan'
,'peoples'
,'peoples r china'
                        
,'Lao Peoples Democratic Republic'
,'Macao'
,'Malaysia'
,'Maldives'
,'Myanmar'
,'Nepal'
,'Philippines'
,'Singapore'
,'Korea Republic of'
,'Sri Lanka'
,'sri'                        
,'Taiwan'
,'Thailand'
,'Timor Leste'
,'VietNam']

dict_continent['oceana']=['American Samoa'
,'Australia'
,'Cook Islands'
,'Fiji'
,'Kiribati'
,'Micronesia Federated States of'
,'Nauru'
,'New Zealand'
,'Niue'
,'Northern Mariana Islands'
,'Palau'
,'Papua n guinea'
,'Samoa'
,'Solomon Islands'
,'Tonga'
,'Tuvalu'
,'Vanuatu']
    
dict_continent['south america']=['south','Argentina'
,'Bolivia'
,'Brazil'
,'Chile'
,'Colombia'
,'Ecuador'
,'French Guiana'
,'Guyana'
,'Mexico'
,'Paraguay'
,'Peru'
,'Suriname'
,'Uruguay'
,'Venezuela']

dict_continent['north america']=['u','new','Aruba'
,'Bahamas'
,'Barbados'
,'Belize'
,'Bermuda'
,'Canada'
,'Cayman Islands'
,'Costa Rica'
,'Dominica'
,'Dominican Republic'
,'El Salvador'
,'Grenada'
,'Guadeloupe'
,'Guatemala'
,'Haiti'
,'Honduras'
,'Jamaica'
,'Martinique'
,'Mexico'
,'Nicaragua'
,'Panama'
,'Puerto Rico'
,'Saint Kitts and Nevis'
,'Saint Vincent and the Grenadines'
,'Saint Lucia'
,'Trinidad and Tobago'
,'Turks and Caicos Islands'
,'United States'
,'United States Minor Outlying Islands'
,'Virgin Islands'
,'usa']

dict_continent['europe']=['rep','russia','serbia','syria','scotland','Albania','north ireland'
,'Andorra'
,'Anguilla'
,'Antarctica'
,'Antigua and Barbuda'
,'Armenia'
,'Austria'
,'Azerbaijan'
,'Belarus'
,'Belgium'
,'Bosnia and Herzegovina'
,'Bouvet Island'
,'British Indian Ocean Territory'
,'Bulgaria'
,'Christmas Island'
,'Cocos (Keeling) Islands'
,'Croatia'
,'Cyprus'
,'czech'                          
,'Czech Republic'
,'Denmark'
,'Estonia'
,'england'
,'byelarus'                    
,'Faroe Islands'
,'Falkland Islands (Malvinas)'
,'Finland'
,'France'
,'French Polynesia'
,'French Southern Territories'
,'Georgia'
,'Germany'
,'Gibraltar'
,'Greece'
,'Greenland'
,'Guam'
,'Heard Island and McDonald Islands'
,'Holy See (Vatican City State)'
,'Hungary'
,'Iceland'
,'Ireland'
,'Italy'
,'Kazakhstan'
,'Kyrgyzstan'
,'Latvia'
,'Liechtenstein'
,'Lithuania'
,'Luxembourg'
,'Macedonia, the former Yugoslav Republic of'
,'Malta'
,'Marshall Islands'
,'Mayotte'
,'Moldova Republic of'
,'Monaco'
,'Mongolia'
,'Montserrat'
,'Netherlands'
,'Netherlands Antilles'
,'New Caledonia'
,'Norfolk Island'
,'Norway'
,'Pitcairn'
,'Poland'
,'Portugal'
,'Reunion'
,'Romania'
,'Russian Federation'
,'ussr'
,'yugoslavia'                          
,'Saint Pierre and Miquelon'
,'Saint Helena'
,'San Marino'
,'Slovakia'
,'Slovenia'
,'Spain'
,'Svalbard and Jan Mayen'
,'Sweden'
,'Switzerland'
,'Tokelau'
,'Turkey'
,'Ukraine'
,'United Kingdom'
,'Wallis and Futuna','wales']

dict_continent['middle east']=['iran','Bahrain'
,'Egypt'
,'Israel'
,'Jordan'
,'Kuwait'
,'Lebanon'
,'Oman'
,'Pakistan'
,'Qatar'
,'saudi'                               
,'Saudi Arabia'
,'Tajikistan'
,'Turkmenistan'
,'United Arab Emirates'
,'u arab emirates'                               
,'Uzbekistan'
,'Western Sahara'
,'Yemen']

dict_continent['africa']=['Algeria'
,'Angola'
,'Benin'
,'Botswana'
,'Burkina Faso'
,'Burundi'
,'Cameroon'
,'Cape Verde'
,'Central African Republic'
,'Chad'
,'Comoros'
,'Congo'
,'Cote d Ivoire'
,'Djibouti'
,'Equatorial Guinea'
,'Eritrea'
,'Ethiopia'
,'Gabon'
,'Gambia'
,'Ghana'
,'Guinea'
,'Guinea Bissau'
,'Kenya'
,'Lesotho'
,'Liberia'
,'Madagascar'
,'Malawi'
,'Mali'
,'Mauritania'
,'Mauritius'
,'Morocco'
,'Mozambique'
,'Namibia'
,'Niger'
,'Nigeria'
,'Rwanda'
,'Sao Tome and Principe'
,'Senegal'
,'Seychelles'
,'Sierra Leone'
,'Somalia'
,'South Africa'
,'Swaziland'
,'Tanzania United Republic of'
,'Togo'
,'Tunisia'
,'Uganda'
,'Zambia'
,'Zimbabwe']


dict_country=dict()

for k, v in dict_continent.iteritems():
    temp=list()
    for co in v:
        temp.append(co.lower())
    dict_continent[k]=temp
        
#print dict_continent['middle east']
    
filename=sys.argv[1]
fo=open(filename,'rb')
reader=csv.reader(fo)

for row in reader:
    for k,v in dict_continent.iteritems():
        temp=v
        if str(row[0]) in temp:
            dict_country[str(row[0])]=k
            break

fo.close()
dict_country['oman']='middle east'
dict_country['romania']='europe'
##dict_country['north ireland']='europe'
dict_country['south korea']='middle east'
filename=sys.argv[2]
fo=open(filename,'rb')
reader=csv.reader(fo)
dict_country['Peoples R China']='asia'
dict_country['rep of georgia']='north america'
##dict_country['czech republic']='europe'
##dict_country['new zealand']='europe'
year_counter=1991

outer_dict=dict()
for q in range(0,20):
    for row in reader:
        co=row[8].split(',')
        year=row[4].split(' ')
        yearf=year[len(year)-1].strip()
        if re.search(r'[A-Z a-z]+',' '.join(co)):
            co=list(set(co))
            new_cou=list()
            for c in co:
                c=c.strip()
                new_cou.append(c)

            for c in new_cou:

                for k1,v1 in dict_continent.iteritems():
                    if str(c) in v1:
                        dict_country[str(c)]=str(k1)
                        break

                
                if outer_dict.has_key(str(yearf)):
                    td=outer_dict[str(yearf)]
                    continent=dict_country[str(c)]
                    flag=0
                    for k,v in td.iteritems():
                        if str(continent)==str(k):
                            td[k]+=1
                            flag=1
                    if flag==0:
                        td[continent]=1
                    outer_dict[str(yearf)]=td
                else:
                    td=dict()
                    td[dict_country[str(c)]]=1
                    outer_dict[str(yearf)]=td
                
                
                
    year_counter+=1        
        
list_continents=['oceana','asia','middle east','africa','north america','south america','europe']


bar_dict=dict()
for k in list_continents:
    year=1991
    #print name
    name=list()
    for t in range(0,20):
        temp=outer_dict[str(year)]
        if temp.has_key(str(k)):
            name.append(int(temp[str(k)]))
            
        else:
            name.append((int(0)))
            
        year+=1
    bar_dict[str(k)]=tuple(name)

ind = np.arange(20)    
width = 0.35
##print bar_dict['oceana']
##print bar_dict['asia']
##print bar_dict['middle east']
##print bar_dict['africa']
##print bar_dict['north america']
##print bar_dict['south america']
##print bar_dict['europe']
a1=bar_dict['oceana']
a2=bar_dict['asia']
a3=bar_dict['middle east']
a4=bar_dict['africa']
a5=bar_dict['north america']
a6=bar_dict['south america']
a7=bar_dict['europe']

b1=list()
b2=list()
b3=list()
b4=list()
b5=list()
b6=list()
b7=list()
for i in range(0,20):
    total=a1[i]+a2[i]+a3[i]+a4[i]+a5[i]+a6[i]+a7[i]
    b1.append((float(a1[i])/float(total))*100)
    b2.append((float(a2[i])/float(total))*100)
    b3.append((float(a3[i])/float(total))*100)
    b4.append((float(a4[i])/float(total))*100)
    b5.append((float(a5[i])/float(total))*100)
    b6.append((float(a6[i])/float(total))*100)
    b7.append((float(a7[i])/float(total))*100)
    i+=1

b1=np.array(b1)
b2=np.array(b2)
b3=np.array(b3)
b4=np.array(b4)
b5=np.array(b5)
b6=np.array(b6)
b7=np.array(b7)

p1 = plt.bar(ind, b1,   width, color='red')

p2 = plt.bar(ind, b2, width, color='yellow',
             bottom=b1)

p3 = plt.bar(ind, b3, width, color='green',
             bottom=b2+b1)

p4 = plt.bar(ind, b4, width, color='orange',
             bottom=b3+b2+b1)

p5 = plt.bar(ind, b5, width, color='indigo',
             bottom=b4+b3+b2+b1)

p6 = plt.bar(ind, b6, width, color='beige',
             bottom=b5+b4+b3+b2+b1)

p7 = plt.bar(ind, b7, width, color='blue',
             bottom=b6+b5+b4+b3+b2+b1)
plt.xlabel('Years')
plt.ylabel('Percentage of journals of each continent')
plt.title('Publications by each continent in every year')
plt.xticks(ind+width/2., ('91', '92', '93', '94', '95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10') )
plt.legend( (p1[0], p2[0],p3[0],p4[0],p5[0],p6[0],p7[0]), ('oceana', 'asia','middle east','africa','north america','south america','europe') )
plt.show()
