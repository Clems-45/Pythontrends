class bedRoom:

   temp1=0
   pur1=0
   bedwash=0


   def __init__(self,temp1,pur1,bedwash):
      self.temp1=temp1
      self.pur1=pur1
      self.bedwash=bedwash

   def getdatpass(self) :
       print("request is being processed ")

   def functiondatpas(self):
       if self.temp1==27 :
          print ("Bedroom has ideal temperature ")
       elif self.temp1>=28 or self.temp1<=26:
         print ("Bedroom Temperature is not ideal ,either too low or too cold. ")
         print  ("Please to adjust the temperature to the optimum temperature ")

# creating instance of objects 
       

#calling functions
temp1 = int(input("enter the temp"))
pur1 = int(input("enter the purity"))
bedwash = int(input("enter the bedwash"))

overalldat1=bedRoom(temp1,pur1,bedwash)
overalldat1.getdatpass()

overalldat1.functiondatpas()





