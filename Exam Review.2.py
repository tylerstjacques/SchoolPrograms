def getinput():
    user_input = int(input('enter an integer between 1 and 10, inclusive'))
    while user_input < 1 or user_input > 10:
        user_input = int(input('enter an integer between 1 and 10, inclusive'))
    print(user_input)


getinput()
