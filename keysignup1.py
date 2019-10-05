color_key={'purple':5,'blue':1,'red':2,'yellow':3}
b=0 # this is for initialization before the highest value from file is passed to b
b=5  # the value '5' is the highest value stored onto a file that can be loaded unto the namespace
# for the function to work with the next time
#

passKey={5:'6rt'}



color_key['orange']= b


d=color_key.keys()
print (d)

f=color_key.values()
print(f)

#the highest value  will be loaded from the file and passed to be
#there is an increment for new key assingment
b=b+1
print(b)

# create a or unique variable or list  that will store the highest  value of which you assigned already to it
# and b will be picking its value from there , b will return it value after the operation to be stored there
# let the unique value be called 'keysignuptempb1'
# the value of this unique value can be written onto a file where  it can loaded next time the sile
# starts so the function can pick and work with values at that location #

keysignuptempb1=b
print (keysignuptempb1)
