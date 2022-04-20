
def factorial(n):
   if n == 1:
       return n
   else:
       return n * factorial(n - 1)

num = 20

if num < 0:
   print("No factorial for negative.")
elif num == 0:
   print("Factorial of 0 is 1")
else:
   print("Factorial: " + str(factorial(num)))