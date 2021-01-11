def main():
    for int in range(101):
        odd_t = threes(int)
        odd_f = fives(int)
        print(int)


def threes(x):
    if int % 3 == 0:
        int = "fizz"
        return int


def fives(y):
    if int % 5 == 0:
        int = "buzz"
        return int


main()
