def iterative_fibonacci(n):
    term1 = 0
    term2 = 1
    for nums in range(n):
        term1, term2 = term2, (term1 + term2)
    return term1


print(fibonacci(12))
print(fibonacci(22))
print(fibonacci(50))
