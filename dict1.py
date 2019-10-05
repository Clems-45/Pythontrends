#!/usr/bin/python

# dictionaries are one step a complex type of list, with its index
# already specified which you have to do , so anytime you referring a certain element you dont have to use index no.s
# not the {} bracket being used

dicta = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dicta['Name']", dicta['Name'])
print("dicta['Age']", dicta['Age'])

print(dicta)
# append to dictionary with its own  key ,using same key will overwrite value with that same key,
# dicta['email']
dicta['email'] = "zaralarsson@gmail.com"
print(dicta)

if 'address' not in dicta.keys():
    dicta['address'] = 'east legon hills'

print(dicta)
