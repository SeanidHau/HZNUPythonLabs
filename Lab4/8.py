def main() :
    sum = 0.0
    term = 1.0
    i = 0
    sign = 1
    while abs(term) > 0.000001 :
        term = sign * (1.0 / (i * 3 + 1))
        sum += term
        sign *= -1
        i += 1
    print(f"{sum:.6f}")


if __name__ == "__main__" :
    main()