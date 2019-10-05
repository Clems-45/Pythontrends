#!/usr/bin/python

class trymike:

      guest=[]
      name =""
      

      while name!="Done":
          name=input("enter name (Enter Done if no more names)")
          guest.append(name)
          guest.sort()
           

          if name=="Done":
             guest.remove("Done")
             
          continue
          
          print(guest)
          

      
           
         
         