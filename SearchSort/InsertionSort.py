def insertion(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0 and value < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = value
    return list


list = [14,59,20,13,42]
print("Unsorted: ", list)

print("Sorted: ", insertion(list))