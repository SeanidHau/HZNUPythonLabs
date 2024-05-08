def main() :
    for line in iter(input, ''):
        a, b = map(int, line.split())
        print(a + b)


if __name__ == "__main__" :
    main()