var1 = [[2, 3, 1],
     [9, 3, 4],
     [7, 5, 4]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for a in range(len(var1)):
   for b in range(len(var1[0])):
          result[b][a] = var1[a][b]

for res in result:
   print(res)