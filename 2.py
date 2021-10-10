# Ryan Scarbrough
# Last Edited: 9/30/21

fibs = [1, 1]
even_fibs = []
while fibs[-1] < 4000000:
    val = fibs[-1] + fibs[-2]
    fibs.append(val)
for i in fibs:
    if i%2 == 0:
        even_fibs.append(i)
print(sum(even_fibs))
