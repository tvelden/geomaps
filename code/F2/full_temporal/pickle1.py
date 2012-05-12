
import pickle
import re
import csv, sys

year=1991
file_year=sys.argv[3]
filename=sys.argv[2]
for t in range(0,19):
    list_of_numbers=list()
    count3=0
    with open(filename, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           count3=count3+1
           temp1=list()
           temp1=row[0].split('\n')
           temp2=row[1].split(' ')
           if re.search(str(year),temp2[len(temp2)-1]) or re.search(str(year+1),temp2[len(temp2)-1]):
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


