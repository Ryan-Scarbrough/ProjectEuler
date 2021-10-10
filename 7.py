import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

primes = []
i = 1
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[-2])
