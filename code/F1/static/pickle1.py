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
import csv, sys
dict1 = pickle.load( open( sys.argv[1], "rb" ) )
cluster_no=sys.argv[4]
cluster_dict=dict()
cluster_dict["1"]=int(0)
cluster_dict["2"]=int(2)
cluster_dict["3"]=int(1)
cluster_dict["4"]=int(3)
cluster_dict["5"]=int(4)
cluster_dict["6"]=int(6)
cluster_dict["7"]=int(7)
cluster_dict["8"]=int(5)



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
for i in range(0,8):
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
    print len(v)
    if no==cluster_dict[cluster_no]:
        print cluster_no
        first_list_ref=v
        break
    no=no+1
    

print "length of reference"    
print len(first_list_ref)


filename = sys.argv[3]
list_of_numbers=list()
count3=0
with open(filename, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       count3=count3+1
       temp1=list()
       temp1=row[0].split('\n')
       #print temp1[0]
       if temp1[0] in first_list_ref:
           list_of_numbers.append(count3)
           

print "great"
fo=open(sys.argv[5],'wb')
csvWriter=csv.writer(fo)
print list_of_numbers[0]

fo1=sys.argv[2]
with open(fo1, 'rb') as f:
   reader = csv.reader(f)
   for row in reader:
       if int(row[0]) in list_of_numbers:
           #print "entered"
           csvWriter.writerow(row)


