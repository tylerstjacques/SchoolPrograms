def main():
    n = int(input())
    forty_two(n)


def forty_two(x):
    n = 42
    total = 0
    while total < x:
        total += 1
        print(n)


main()
