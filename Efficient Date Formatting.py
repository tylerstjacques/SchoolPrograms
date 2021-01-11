months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
            '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

string = input('Enter date in mm/dd/yyyy format: ')
list = string.split('/')

newList = []
for strings in list:
    if len(strings) == 1:
        strings = '0' + strings
        newList.append(strings)
    else:
        newList.append(strings)

print('Here is your formatted date: ' + months[newList[0]] + ' ' + newList[1] + ', ' + newList[2])
