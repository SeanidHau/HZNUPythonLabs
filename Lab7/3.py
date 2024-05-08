def main() :
    s = input().strip()
    count = 0
    for c in s :
        if c.isdigit() :
            count = count * 10 + int(c)
    print(count)


if __name__ == '__main__' :
    main()