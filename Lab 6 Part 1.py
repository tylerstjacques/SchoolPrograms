numList = [0, 1, 2, 3, 4, 5]


def sortCheck(numList):
    for element in numList:
        num = element
        num1 = numList.index(num)
        num2 = numList.index(num+1)
        if num1 > num2:
            return False
        else:
            continue
        return True


trueFalse = sortCheck(numList)
print(trueFalse)
