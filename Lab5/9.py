def square_root(value, last = 1.0) :
    next = 0.5 * (last + value / last)
    if (abs(last - next) < 1e-6) :
        return next
    return square_root(value, next)