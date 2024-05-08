def main() :
    a, n = map(int, input().split())
    sum = 0
    while n > 0 :
        num = 0
        for _ in range(n) :
            num = num * 10 + a
        sum += num
        n -= 1
    print(sum)


if __name__ == "__main__" :
    main()