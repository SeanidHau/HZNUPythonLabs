def main() :
    s = set(map(int, input().split(",")))
    full_s = set(range(6, 11))
    missing = list(full_s - s)
    if missing :
        for num in sorted(missing) :
            print(num, end = " ")


if __name__ == "__main__" :
    main()