def average(lst):
    sum = 0
    for int in lst:
        sum = sum+int
    avg = sum / len(lst)
    print(avg)


lst = []
user_input = int(input('Enter an integer, 0 to break'))
while user_input < 0 or user_input > 0:
    lst.append(user_input)
    user_input = int(input('Enter an integer, 0 to break'))

average(lst)
