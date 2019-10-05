def sigNuP():


    user_key = {'purple': 5, 'blue': 1, 'red': 2, 'yellow': 3}


    passKey = {5: '6rt'}

    b = 0

    d = user_key.keys()
    print (d)

    f = user_key.values()
    print(f)

    for x in f:
        # we can add append list to store them in order
        # #we have to create that order for now we just want the highest
        if b < x:
            b = x
        # the b has to be executed outside the for loop other than that it would add + 1 to
        # b for every step of b computed which would give a final value of 10
    b = b + 1
    print(b)

    username = input('enter username or email')
    password = input('enter password ')

    user_key[username] = b
    passKey[b] = password

    #  NB THE new updated addition will stay in the namespace during the function
    # or software is being run but has to be written onto a permanent file storage which will
    # pick it up and load during the next time the file has to be run
    # these dictionaries  being printed now might be saved onto a file and loaded next time b4 the function
    # so the function can load values and infer from there #
    print(user_key)
    print(passKey)
    print('proceed to login')




