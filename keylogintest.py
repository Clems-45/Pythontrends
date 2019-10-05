def loGtest():


    user_key = {'purple': 5, 'blue': 1, 'red': 2, 'yellow': 3}


    passKey = {5: 'rt'}




    uSerName = input('enter username ')
    paSsword = input('enter password')
    pkey=0
    d = user_key.keys()
    print (d)

    f = user_key.values()
    print(f)

    for x in f:
        # we can add append list to store them in order
        # #we have to create that order for now we just want the highest
        if uSerName == x:
            ukey = user_key[x]
            # temporary value 'ukey' to hold key , variable will be used later to find the password
            # and comparison made for a match and the function can proceed
            pkey = passKey[ukey]

            if pkey == paSsword:
                print('congrats you gained entrance to the system ')
                print('proceed to login')
                # next function can be loaded
            elif pkey != paSsword:
                print ('wrong password')

        elif uSerName != x :
            print('enter right username or email ')


    print ('pkey')






    #  NB THE new updated addition will stay in the namespace during the function
    # or software is being run but has to be written onto a permanent file storage which will
    # pick it up and load during the next time the file has to be run
    # these dictionaries  being printed now might be saved onto a file and loaded next time b4 the function
    # so the function can load values and infer from there #

