n = 100
total1 = 0
for i in range(1, n+1):
    total1 += i**2
total2 = 0
total3 = 0
for i in range(1, n+1):
    total2 += i
total3 = (total2)**2
final = total3 - total1
print(final)
