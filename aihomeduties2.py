#!/usr/bin/python

class  bedroom:


#            this class enables us to automate the duties
#                    in the bedroom


#          1.  Accept input from user and store in list ,
#           which might be converted to tuple
      list = []

      temper1=int(input("please enter the temp"))

      list.append(temper1)
      print (list )


      pure1=int(input("please enter the purity"))

      list.append(pure1)
      print (list)


         #   accept variable values as input

      bedwash1=int(input("please enter the state of bedwashroom"))

      list.append(bedwash1)
      print (list)



           #  2. Now to initialize  create methods and functions


           #    A. First determine the locations of the various elements in a list

      print (list[0])
      print (list[1])
      print (list[2])
      print (list[:])



      print (list)
      def tempcheck(self,newList):
          temp=newList[0]
          if  temp==27:
           print ("Bedroom has ideal temperature ")
          elif temp>=28 or temp<=26:
             	      print ("Bedroom Temperature is not ideal ,either too low or too cold. ")
             	      print  ("Please to adjust the temperature to the optimum temperature which is 27 degree Celsuis")


             # now to initialize args
      def __init__ (self, temp, puri1, bedwashroom, newList):
           self.temp=temp
           self.puri1=puri1
           self.bedwashroom=bedwashroom

           tempcheck(newList)




            # now calling the functions

          # newvalue=tempcheck(list)

            #   B.











