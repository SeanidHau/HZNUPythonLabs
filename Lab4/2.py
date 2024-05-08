def main() :
    n = int(input())
    while n > 0 :
        a, b = map(int, input().split())
        print(a + b)
        n -= 1


if __name__ == "__main__" :
    main()