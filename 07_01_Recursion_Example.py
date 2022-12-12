def backwardsby2(num):
    #At the start a condition to exit (a 'BASE CASE') - this is cruical!
    if num <= 0:
        print('Zero!')
        return

    #Then the main code to execute on each recursion:
    else:
        emojismiles = []
        for i in range(0, num):
            emojismiles += '😃'
        print(num, ' '.join(emojismiles))

    #Finally call the function with a modification to the paramaters
    # (in this case reduce num by 2 and proceed)
        backwardsby2(num - 2)

# 'Driver Code' - calls the funtion and sets the paramater (num) to its
#  starting value.
backwardsby2(9)
