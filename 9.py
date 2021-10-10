for i in range(998):
    for j in range(998):
        for k in range(998):
            if i < j and j < k:
                if i**2 + j**2 == k**2 and i+j+k == 1000:
                    print(i * j * k)
                    break
