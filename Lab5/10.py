def f(x, n) :
    if n == 1 :
        return  x
    return (-1) ** (n-1) * x ** n + f(x, n - 1)