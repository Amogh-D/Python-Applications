var1 = [[2, 3, 1],
     [9, 3, 4],
     [7, 5, 4]]

var2 = [[9, 5, 42],
     [21, 43, 62],
     [49, 94, 14]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for m in range(len(var1)):
   for n in range(len(var2[0])):
          for o in range(len(var2)):    
               result[m][n] += var1[m][o] * var1[o][n]

for res in result:
   print(res)