def split(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x

arr = [40,20,19,49,34]
n = len(arr)
value = 5

split(arr, n, value)

for i in range(0, n):
    print(arr[i], end = ' ')