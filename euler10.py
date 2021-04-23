# euler 10
# KeyJect
import math
def isPrime(num):
  for i in range(2 , int(math.sqrt(num)+1)):
    if num%i==0:
      return False
  return True

i = 5
sumPrime = 5
while i<2000000:
  if isPrime(i):
    sumPrime += i
  i += 2
print(sumPrime)