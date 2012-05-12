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
dict1 = pickle.load( open( sys.argv[1], "rb" ) )

cluster_no=sys.argv[4]
cluster_dict=dict()
cluster_dict["1"]=int(2)
cluster_dict["2"]=int(3)
cluster_dict["3"]=int(4)
cluster_dict["4"]=int(6)
cluster_dict["5"]=int(7)
cluster_dict["6"]=int(8)
cluster_dict["7"]=int(5)
cluster_dict["8"]=int(9)
cluster_dict["9"]=int(10)
cluster_dict["10"]=int(0)
cluster_dict["11"]=int(1)

count=0
#print dict1
count1=list()
for k,v in dict1.iteritems():
    #print v
    #type(v)
    count1.append(len(v))
    count=count+1

count1.sort(reverse=True)
print"great"

new_count1=list()
for i in range(0,11):
    new_count1.append(count1[i])
    
new_dict=dict()
count2=0
for k,v in dict1.iteritems():
    if len(v) in new_count1:
        new_dict[k]=v
        count2=count2+1
    

print count2
first_list_ref=list()
no=0
for k, v in new_dict.iteritems():
    if no==cluster_dict[cluster_no]:
        first_list_ref=v
        print len(v)
        break
    no+=1
    
print first_list_ref[0]

file_year=sys.argv[5]
filename = sys.argv[3]

year=1991

for t in range(0,19):
    #print "mahan"
    list_of_numbers=list()
    count3=0
    with open(filename, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           count3=count3+1
           temp1=list()
           temp1=row[0].split('\n')
           temp2=row[1].split(' ')
           if temp1[0] in first_list_ref and (re.search(str(year),temp2[len(temp2)-1]) or re.search(str(year+1),temp2[len(temp2)-1])):
               list_of_numbers.append(count3)
               #print row[1]
               

    #print "great"
    fo=open(file_year+str(year)+".csv",'wb')
    csvWriter=csv.writer(fo)
    #print list_of_numbers[0]

    fo1=sys.argv[2]
    with open(fo1, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           if int(row[0]) in list_of_numbers:
               #print "entered"
               csvWriter.writerow(row)

    year+=1

