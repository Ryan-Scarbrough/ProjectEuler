import math

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

# print(isPrime(4))
tot = 0
for i in range(1, 2000000):
    if isPrime(i):
        tot += i

print(tot)
