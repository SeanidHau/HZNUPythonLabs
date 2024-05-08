def main() :
    while True :
        line = input()
        num = list(map(int, line.split()))
        if num[0] == 0 :
            break
        s = sum(num[1:])
        print(s)


if __name__ == "__main__" :
    main()