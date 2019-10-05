#!/usr/bin/python

list1=['physics', 'chemistry',1997,2000];
list2=[1,2,3,4,5,6,7] ;

#append contents to seq starts from here 
list1.extend(list2)
print ("extended list :") , list1
#end of the appending to seq code. 

print("list1[0]:" ), list1[0]
print ("list2[1:5]:") , list2[1:5]

print (list1.count("physics"))
print (len(list2[1:5]))

print (list1[1:3].count("physics"))


  

for x in [1,2,3]:
	print (x) ,


replist1=['hi']*4

for x in  replist1:
	print (x),


# indexing and  , slicing (seenon line 27)of elements of array, 

L=['spam','Spam','SPAM']

print (L[2] , L[-2] , L[1:])


list1.insert(2,"biology");
print (list1)

print (list2)
print (list1)
