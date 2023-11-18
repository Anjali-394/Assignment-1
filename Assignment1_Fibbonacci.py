 Write a Python program to get the Fibonacci series between 0 to 50

def fibbonacci(n):
   seed1 = 0
   seed2 = 1 
   if n == 1:
      print(seed1)
   else:
      print(seed1)
      print(seed2)
      while seed2 < 50:
         print (seed2)
         seed1, seed2 = seed2, seed1 + seed2

fibbonacci (50)