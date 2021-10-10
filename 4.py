# Ryan Scarbrough
# Last Edited: 10/1/21

fred = [0]
for i in range(999):
    for j in range(999):
        num = i * j
        if str(num) == str(num)[::-1] and num > fred[-1]:
            fred.append(num)
print(fred[-1])
