def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n - 1) + fibonacci(n - 2))

totalTerms = 10

if totalTerms <= 0:
   print("Enter Value: ")
else:
   print("Fibonacci Sequence: ")
   for i in range(totalTerms):
       print(fibonacci(i))