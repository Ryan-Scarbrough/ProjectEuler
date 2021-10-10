import math

num = 600851475143

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

i = 2
factors = []
while i < math.ceil(math.sqrt(num)):
    if num % i == 0:
        thing = num % i
        if thing == 0 and isPrime(i):
            factors.append(i)
        if isPrime(num/i):
            i = num/i
            factors.append(i)
    i += 1
print(max(factors))
