def sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)

array = []
array = [12, 3, 4, 15]
n = len(array)
ans = sum(array)

print('Sum of Array:', ans)