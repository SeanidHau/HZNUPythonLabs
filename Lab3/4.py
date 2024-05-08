def main() :
    n = eval(input())
    if n < 0 :
        print("Invalid Value!")
    elif n <= 50 :
        print(f"cost = {n * 0.53:.2f}")
    else :
        print(f"cost = {50 * 0.53 + (n - 50) * 0.58:.2f}")


if __name__ == "__main__" :
    main()