def main() :
    a, b = map(int, input().split())
    numRange = b - a + 1
    count = 0
    sum = 0
    for i in range(a, b + 1) :
        print(f"{i:>5}", end = '')
        count += 1
        if count == 5 :
            print()
            count = 0
        sum += i
    if numRange % 5 != 0 :
        print()
        print("Sum = ", sum ,sep = '')
    else :
        print("Sum = ", sum ,sep = '')

if __name__ == "__main__" :
    main()