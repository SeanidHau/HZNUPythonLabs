def main() :
    n = int(input())
    while n > 0 :
        line = input()
        num = list(map(int, line.split()))
        s = sum(num[1:])
        print(s)
        n -= 1


if __name__ == "__main__" :
    main()