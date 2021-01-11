userPass = input('Please enter a password (press [enter] to finish):')

passList = []
while userPass != '':
    userPass = input('Please enter a password (press [enter] to finish):')
    passList.append(userPass)


starList = []
for passwords in passList:
    for ch in passwords:
        ch = '*'
    starList.append(passwords)

print(passList)
print(starList)
