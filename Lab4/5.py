def main() :
    n = int(input())
    sum = 0
    for i in range(1, n + 1) :
        sum += 1 / (2 * i - 1)
    print(f"{sum:.3f}")


if __name__ == "__main__" :
    main()