def main() :
    money = eval(input())
    year = eval(input())
    rate = eval(input())
    interest = money * ((1 + rate) ** year) - money
    print(f"{interest:.2f}")


if __name__ == "__main__" :
    main()