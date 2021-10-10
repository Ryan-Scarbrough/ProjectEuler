def collatz(n):
    times = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        times += 1
    return times

max = 0
ans = 0
for i in range(1, 1000000): # 1 m
    fred = collatz(i)
    if fred > max:
        max = fred
        ans = i
print(ans)
