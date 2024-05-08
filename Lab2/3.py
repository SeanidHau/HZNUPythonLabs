def main() :
    a = int(input())
    b = int(input())
    print(f"{a + b}", f"{(a + b) / 2:.2f}", f"{min(a, b)}", f"{max(a, b)}",sep='\n')


if __name__ == "__main__" :
    main()