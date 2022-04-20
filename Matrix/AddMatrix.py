var1 = [[2, 3, 1],
     [9, 3, 4],
     [7, 5, 4]]

var2 = [[9, 5, 42],
     [21, 43, 62],
     [49, 94, 14]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(var1)):
    for j in range(len(var1[0])):
        result[i][j] = var1[i][j] + var2[i][j]
for r in result:
    print(r)