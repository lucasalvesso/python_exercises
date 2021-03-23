def mmc(a, b, i):
    # recursiva e não recursiva
    total = 1
    while (a * i) % b > 0:
        i += 1
        total = a * i
    return total
    # if ((a * i) % b) == 0:
    #     return a * i
    # else:
    #     return mmc(a, b, i+1)

print(mmc(29, 18, 1))