

class bedroom:
#this class enables us to automate the duties
# in the bedroom 

#   accept variable values as input 

   def __init__(self,temp,purity,bedwashroom):
    	
         self.temp=temp
    	 self.purity=purity
    	 self.bedwashroom=bedwashroom
   

#    1 store 2 print   values 
   def printupl(self):
         
          bedtuple=();

          self.temp=int(input("please enter the temp"))
          bedtuple=bedtuple + (self.temp,)

          self.purity=input("please enter the purity state")
          bedtuple=bedtuple + (self.purity,)

          self.bedwashroom=int(input("please enter the bedwashroom state"))
          bedtuple=bedtuple + (self.bedwashroom,)


          print bedtuple


#declare the tuple over here 

        
 

#       append the input to new tuple locations.

       
         


#we do this for the next succession of inputs 

        
         

        
         
          
         


#    after everything  we del the bedtuple 
#       for next cyle 
    	  del bedtuple
    	  return;

printupl(self)

  
