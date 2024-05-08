def main() :
    user_input = input()
    a, b = map(int, user_input.split(','))
    while b > 0 :
        print(a, end = '')
        b -= 1


if __name__ == "__main__" :
    main()