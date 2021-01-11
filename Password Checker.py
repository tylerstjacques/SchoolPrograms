def password():
    userPassword = input('Please enter a password:')
    cream = check(userPassword)
    if cream == True:
        print('Password accepted')
    else:
        continue


def check(userPassword):
    while 8 <= len(userPassword) <= 20:
        caseBool = case(userPassword)
        numBool = number(userPassword)
        spaceBool = space(userPassword)
        specharBool = special_characters(userPassword)
        if caseBool == True and numBool == True and spaceBool != True and specharBool == True:
            finalCheck = True
            return finalCheck
        else:
            password()



def case(userPassword):
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
    for character in userPassword:
        for letter in cap_letters:
            if character == letter:
                return True


def number(userPassword):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for character in userPassword:
        for number in numbers:
            if character == number:
                return True


def space(userPassword):
    space = [' ']
    for char in userPassword:
        for sp in space:
            if char == sp:
                return True


def special_characters(userPassword):
    symbols = ['!', '?', ',', '.', ';', ':', '$', '#', '&']
    for ch in userPassword:
        for sym in symbols:
            if ch == sym:
                return True


password()
