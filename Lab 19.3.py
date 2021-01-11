import random
f = open('Lab 19.3', 'w')

lst = []
len_numbers = int(input('How many numbers do you want in your list?'))
total = 0

while total < len_numbers:
    randomInt = random.randint(10, 99)
    lst.append(randomInt)
    total += 1
lst.sort()
f.write(str(lst))
print(lst[-1])
f.close()
