def linear(list, n, key):
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1


list = [43, 9, 32, 54, 24, 15]
key = 15

empty = len(list)
lin = linear(list, empty, key)
if (lin == -1):
    print("Not Found. ")
else:
    print("Index Value:", lin)