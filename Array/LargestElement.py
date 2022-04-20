def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


array = [40,24,10,414,394]
n = len(array)
result = largest(array, n)
print("Largest Element:", result)