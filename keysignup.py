color_key={'purple':5,'blue':1,'red':2,'yellow':3}
b=0

passKey={5:'6rt'}





d=color_key.keys()
print (d)

f=color_key.values()
print(f)

for x in f :
    #we can add append list to store them in order
    # #we have to create that order for now we just want the highest
    if b<x :
       b=x
     # the b has to be executed outside the for loop other than that it would add + 1 to
    # b for every step of b computed which would give a final value of 10
b=b+1
print(b)

username=input('enter username or email')
password=input('enter password ')




color_key[username]= b
passKey[b]=password

#  NB THE new updated addition will stay in the namespace during the function
# or software is being run but has to be written onto a permanent file storage which will
# pick it up and load during the next time the file has to be run  #
print(color_key)
print(passKey)
