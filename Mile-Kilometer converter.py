conversionDirection = input('Hello! Are you converting from miles to kilometers or kilometers to miles?')

if conversionDirection == 'kilometers to miles':
    lengthKilometers = int(input('how many kilometers would you like to convert?'))
    miles = lengthKilometers / 1.6
    print(lengthKilometers, 'kilometers is equal to', miles, 'miles')
else:
    lengthMiles = int(input('how many miles would you like to convert?'))
    kilometers = lengthMiles * 1.6
    print(lengthMiles, 'miles is equal to', kilometers, 'kilometers')
