def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def remake(n):
    factors = []
    factor_powers = []
    re_factor_powers = []
    fredmk2 = 1
    for i in range(2, 100):
        if isPrime(i) and n % i == 0:
            factors.append(i)

    for i in factors:
        retarded = 0
        while n % i == 0:
            retarded += 1
            n = n/i

        factor_powers.append(retarded)

    for i in factor_powers:
        re_factor_powers.append(i+1)

    for i in re_factor_powers:
        fredmk2 *= i
    return fredmk2

nth_tri=1 # starting point
while True:
    triangle_num = 0
    for i in range(nth_tri + 1):
        triangle_num += i
    if remake(triangle_num) > 500:
        print(triangle_num)
        break
    nth_tri += 1
