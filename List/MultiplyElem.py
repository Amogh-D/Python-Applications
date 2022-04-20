def multiply(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

firstList = [4,59,32]
secondList = [94,32,12]
print(multiply(firstList))
print(multiply(secondList))