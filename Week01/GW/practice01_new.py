for num in range(99, -1, -1):
    if num == 0:
        number = 'No more'
    else:
        number = str(num)
    if num != 1:
        plural = 's'
    else:
        plural = ''
    first = number + ' bottle' + plural + ' of beer on the wall, ' + number + ' bottle' + plural + ' of beer.\n'

    if num == 0:
        second = 'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
    else:
        if num - 1 == 0:
            number = 'no more'
            plural = 's'
        elif num - 1 == 1:
            plural = ''
            number = '1'
        else:
            number = str(num - 1)
            plural = 's'
        second = 'Take one down and pass it around, ' + number + ' bottle' + plural + ' of beer on the wall.\n'
    print(first + second)
