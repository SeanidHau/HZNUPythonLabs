def m(i) :
    res = 0
    for i in range(1, i + 1) :
        res += (-1) ** (i + 1) / (2 * i - 1)
    return res