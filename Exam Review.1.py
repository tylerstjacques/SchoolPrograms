def compute(principal, rate, numYears):
    total = 0
    while total < numYears:
        principal = principal*(1+rate)
        total += 1
        return principal


principal = float(input('a'))
rate = float(input('b'))
numYears = int(input('c'))
compute(principal, rate, numYears)


print(principal)
