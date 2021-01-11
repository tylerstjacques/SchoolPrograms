import time


def recursive_fibonacci(n):
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def iterative_fibonacci(n):
    num1 = 0
    num2 = 1
    for nums in range(n):
        num1, num2 = num2, (num1 + num2)
    return num1


n = 29

t1 = time.time()
recursive_fibonacci(n)
t2 = time.time()
print('Recursive runtime', t2-t1)

t1 = time.time()
iterative_fibonacci(n)
t2 = time.time()
print('Iterative runtime', t2-t1)

