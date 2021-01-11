maxValue = 30

userNum = int(input('Enter max value: '))

for nums in range(2,userNum):
    is_prime = True
    for quotient in range(2 , userNum):
        if userNum % quotient == 0:
            is_prime = False
            break
    if is_prime:
        print(userNum, 'is prime')
    else:
        print(userNum, 'is not prime')


primes = []
for userNum in range(2, maxValue):
    is_prime = True
    max_divisor = (userNum / 2) + 1
    for quotient in range(2, max_divisor):
        if userNum % quotient == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(userNum)