def loGtest():


    user_key = {'kelvin@gmail.com': 5, 'blue': 1, 'red': 2, 'yellow': 3}


    passKey = {5: 'rt'}

    pkey=0

   # this gives the set of keys and values that can be displayed for the administrator to see about login details

    d = user_key.keys()


    f = user_key.values()

    print(d)
    print(f)
    #  this is the end  the set containing keys and values which might not be used

    tempUse=0

    uSerName = input('enter username ')

    for x in user_key:
        # we can add append list to store them in order
        # #we have to create that order for now we just want the highest

        if x == uSerName:
            ukey = user_key[x]
            # temporary value 'ukey' to hold key , variable will be used later to find the password
            # and comparison made for a match and the function can proceed

            pkey = passKey[ukey]



            # there should be a variable being passed from out put if this loop if it found the name  worked and if it did not find anything
            tempUse = uSerName



#  we can exit the loop now that we have located the password location and stored it some where to be used later


    if tempUse==uSerName :
        print ('Username is found ')
        paSsword = input('enter password')

        if pkey == paSsword:
            print('congrats you gained entrance to the system ')
            print('proceed to login')
            # next function can be loaded
        elif pkey != paSsword:
            print('wrong password you will be directed back to enter Username allover again')
            loGtest()

    elif tempUse !=uSerName :
         print('enter the right username or email ')
         loGtest()



    #  NB THE new updated addition will stay in the namespace during the function
    # or software is being run but has to be written onto a permanent file storage which will
    # pick it up and load during the next time the file has to be run
    # these dictionaries  being printed now might be saved onto a file and loaded next time b4 the function
    # so the function can load values and infer from there #

