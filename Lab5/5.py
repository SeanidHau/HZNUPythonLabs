def count_digit(number, digit) :
    count = 0
    if number < 0 :
        number *= -1
    while number :
        if number % 10 == digit :
            count += 1
        number //= 10
    return count