def loGiN():


    user_key = {'purple': 5, 'blue': 1, 'red': 2, 'yellow': 3}
    pass_key = {5: '6rt'}

    uSerName='enter username '
    paSsword ='enter password'

    u=user_key.keys

    for x in u :
        if uSerName==x :

            ukey=user_key[x]
            # temporary value 'ukey' to hold key , variable will be used later to find the password
            # and comparison made for a match and the function can proceed
            pkey=pass_key[ukey]



    if pkey==paSsword:
        print('congrats you gained entrance to the system ')
           #next function can be loaded
    elif pkey!=paSsword:
        print ('wrong password')
        sigNuP()
