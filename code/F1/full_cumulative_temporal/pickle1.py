##import jsonpickle
##f=open('C:\Users\chitrita\Desktop\maps\our_project\pickle1.pck')
##json_str=f.read()
##obj = jsonpickle.encode(json_str)
##
##for k,v in obj:
##    
##    print obj
##    break
import pickle
import re
import csv, sys

year=1991
file_year=sys.argv[3]
filename=sys.argv[2]
for t in range(0,20):
    list_of_numbers=list()
    count3=0
    with open(filename, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           count3=count3+1
           temp1=list()
           temp1=row[0].split('\n')
           temp2=row[1].split(' ')
           if int(temp2[len(temp2)-1])<=int(year):
               list_of_numbers.append(count3)
               #print row[1]
               

    #print "great"
    fo=open(file_year+str(year)+".csv",'wb')
    csvWriter=csv.writer(fo)
    #print list_of_numbers[0]

    fo1=sys.argv[1]
    with open(fo1, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           if int(row[0]) in list_of_numbers:
               #print "entered"
               csvWriter.writerow(row)

    year+=1

##fo=open('final_eight_clusters.csv','wb')
##csvWriter = csv.writer( fo )  #Defaults to the excel dialect
##for k, v in new_dict.iteritems():
##    temp=list()
##    temp.append(k)
##    temp.append(v)
##    csvWriter.writerow(temp)


##i=0
##line1=list()
##fi='final_eight_clusters.csv'
##with open(fi, 'rb') as f:
##   reader = csv.reader(f)
##   for row in reader:
##       #print row[1]
##       print len(row[1])
##       line1.append(row[1])
##       i=i+1
##       #print len(row[1])
##       if i==7:
##           break
