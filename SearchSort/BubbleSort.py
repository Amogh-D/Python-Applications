def bubble(list):
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


list = [40,30,20,15,35]
print("Unsorted: ", list)
print("Sorted: ", bubble(list))