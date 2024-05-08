def main() :
    n = int(input())
    print(f"{n} divisible by 2 and 3? {n % 2 == 0 and n % 3 == 0}")
    print(f"{n} divisible by 2 or 3? {n % 2 == 0 or n % 3 == 0}")
    print(f"{n} divisible by 2 or 3, but not both? {(n % 2 == 0 and n % 3 != 0) or (n % 3 == 0 and n % 2 != 0)}")


if __name__ == "__main__" :
    main() 