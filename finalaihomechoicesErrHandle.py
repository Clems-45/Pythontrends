class bedRoom:
    temp1 = 0
    pur1 = 0
    bedwash = 0


    def __init__(self, temp1, pur1, bedwash):
        self.temp1 = temp1
        self.pur1 = pur1
        self.bedwash = bedwash



    def getdatpass(self):
        print("request is being processed ")


    def functiondatTemp(self):
        if self.temp1 == 27:
            print("Bedroom has ideal temperature ")
        elif self.temp1 >= 28 or self.temp1 <= 26:
            print("Bedroom Temperature is not ideal ,either too low or too cold. ")
            print("Please to adjust the temperature to the optimum temperature ")

    def functiondatPur(self):

            if self.pur1 == "neat":
                print("Bedroom is hygienic ")
            elif self.pur1 == "dirty":
                print("Bedroom Temperature is not hygienic  ")
                print("Please to clean the room  ")

                # assign the input which is neither neat nor a  not neat to a variable an raise an exception.





    def functiondatBedwash(self):
        if self.bedwash == 27:
            print("Bedroom has optimum water level ")
        elif self.bedwash >= 28 or self.bedwash<= 26:
            print("Bedroom water is not ideal ,either there is no water or tap is overflowing. ")
            print("Please to adjust the water pump to have optimum water level  ");

    def chooSefunction(self):

            print("enter A for temperature,")
            print("B for purity assessment ")
            print("C for bedroom water level")
            print("D for all options check ")
            print("E for Exit or  move to end class or return nothing and move on to next class maybe other Rooms")
            try:
                bedroMspefs = input(
                    "  Enter choice in Caps over here ")
                # exception to function can be continued here
                # where the error handler can handle any odd choice and and re run the function chooSefunction.

                #this function acts behind the scene to check if a string is been input, if its not it will throw
                #an exception .
                
                reaLcheck=bedRoom +"chicken"
                if bedroMspefs == "A":
                    # check indention in future whether it affects the class
                    overalldat1.functiondatTemp()
                elif bedroMspefs == "B":
                    overalldat1.functiondatPur()
                elif bedroMspefs == "C":
                    overalldat1.functiondatBedwash()
                elif bedroMspefs == "D":
                    overalldat1.functiondatTemp()
                    overalldat1.functiondatPur()
                    overalldat1.functiondatBedwash()

                elif bedroMspefs == "E":
                    print("we will be moving on to the the rooms since you have chosen to exit to other  choices  ")

            except ValueError:
                print ("you have an invalid character which is not a string ")
                print("Enter the right data")

            except TypeError:
                print("you have an invalid character which is not a string ")
                print("Enter the right data")


            finally:
               if bedroMspefs != "A" or bedroMspefs != "B" or bedroMspefs != "C" or bedroMspefs != "D":

            # this will function will be run finally after the variable whether the reaLcheck has escaped the exception or not
            # this will work because of the code says "finally".
                  overalldat1.chooSefunction()






    #       Error handling is first thing done
#       can be be done on the alphabet choice whether if choice is not A or B or C or D then the error should be caught





    #       and print invalid choice and  return user to the choose a right option or alphabet either A or B or C ... also how can i change
    #
    #        return  the function which brings back the enter values side ;

        # i will have to use try statements to catch errors here if user chooses an wrong alphabet he have to
        # to choose again until he has choosing the right one




# creating instance of objects


# calling functions and initializing class to start
temp1 = int(input("enter the temp"))
pur1 = input("enter the purity ,if bedroom is clean,Enter neat in small caps if not enter dirty ")
bedwash = int(input("enter the bedwash"));

overalldat1 = bedRoom(temp1, pur1, bedwash);

overalldat1.chooSefunction()



#







