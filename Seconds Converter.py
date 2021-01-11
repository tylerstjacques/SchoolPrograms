numSeconds = int(input('Please enter the number of seconds: '))

hours = numSeconds // 3600
hoursRemainder = numSeconds % 3600
minutes = hoursRemainder // 60
seconds = hoursRemainder % 60
if hours > 1:
    if minutes > 1:
        if seconds > 1:
            print(hours, 'hours', minutes, 'minutes', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hours', minutes, 'minutes', seconds, 'second')
        else:
            print(hours, 'hours', minutes, 'minutes')
    elif minutes == 1:
        if seconds > 1:
            print(hours, 'hours', minutes, 'minute', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hours', minutes, 'minute', seconds, 'second')
        else:
            print(hours, 'hours', minutes, 'minute')
    else:
        if seconds > 1:
            print(hours, 'hours', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hours', seconds, 'second')
        else:
            print(hours, 'hours')
elif hours == 1:
    if minutes > 1:
        if seconds > 1:
            print(hours, 'hour', minutes, 'minutes', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hour', minutes, 'minutes', seconds, 'second')
        else:
            print(hours, 'hour', minutes, 'minutes')
    elif minutes == 1:
        if seconds > 1:
            print(hours, 'hour', minutes, 'minute', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hour', minutes, 'minute', seconds, 'second')
        else:
            print(hours, 'hour', minutes, 'minute')
    else:
        if seconds > 1:
            print(hours, 'hour', seconds, 'seconds')
        elif seconds == 1:
            print(hours, 'hour', seconds, 'second')
        else:
            print(hours, 'hour')
else:
    if minutes > 1:
        if seconds > 1:
            print(minutes, 'minutes', seconds, 'seconds')
        elif seconds == 1:
            print(minutes, 'minutes', seconds, 'second')
        else:
            print(minutes, 'minutes')
    elif minutes == 1:
        if seconds > 1:
            print(minutes, 'minute', seconds, 'seconds')
        elif seconds == 1:
            print(minutes, 'minute', seconds, 'second')
        else:
            print(minutes, 'minute')
    else:
        if seconds > 1:
            print(seconds, 'seconds')
        elif seconds == 1:
            print(seconds, 'second')