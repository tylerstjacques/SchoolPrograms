def is_leap_year(user_year):
    if user_year % 4 == 0 or (user_year % 100 == 0 and user_year % 400 == 0):
        print(user_year, 'is a leap year')
    else:
        print(user_year, 'is not a leap year')
    return user_year

if __name__ == '__main__':
    user_year = int(input())
    if user_year % 4 == 0 or (user_year % 100 == 0 and user_year % 400 == 0):
        print(user_year, 'is a leap year')
    else:
        print(user_year, 'is not a leap year')
    is_leap_year(user_year)
