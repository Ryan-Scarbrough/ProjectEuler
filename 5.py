num = 2520
ans = 2520

def isDivis(n):
    for i in range(1, 20+1):
        if n % i != 0:
            return False
    return True

while True:
    if isDivis(ans):
        print(ans)
        break
    else:
        ans = ans + num
