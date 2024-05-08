def reverse(n) :
    temp = 0
    if n < 0 :
        n *= -1
        while n != 0 :
            temp = temp * 10 + n % 10
            n = n // 10
        return temp * -1
    else :
        while n != 0 :
            temp = temp * 10 + n % 10
            n = n // 10
        return temp