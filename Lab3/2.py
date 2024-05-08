def main() :
    x, y = map(float, input().split(","))
    if (x - 2) ** 2 + (y - 2) ** 2 <= 1 or (x - 2) ** 2 + (y + 2) ** 2 <= 1 or (x + 2) ** 2 + (y - 2) ** 2 <= 1 or (x + 2) ** 2 + (y + 2) ** 2 <= 1 :
        print(10)
    else :
        print(0)


if __name__ == "__main__" :
    main()