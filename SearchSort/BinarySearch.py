def binary(list, n):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if list[mid] < n:
            low = mid + 1

        elif list[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


list1 = [94,30,42,49,50]
n = 50

result = binary(list1, n)

if result != -1:
    print("Index Value: ", str(result))
else:
    print("Not Found. ")