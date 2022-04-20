def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [23, 65, 19, 90]
firstPos = 0
secPos = 3

print(swap(list, firstPos - 1, secPos - 1))