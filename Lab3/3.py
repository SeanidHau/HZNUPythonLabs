def main() :
    x = eval(input())
    if x < 0 :
        y = x ** 2
    elif x < 9:
        y = x ** 0.5
    else :
        y = x - 6
    print(f"{y:.2f}")


if __name__ == "__main__" :
    main()