def main() :
    list_of_strings = []
    for _ in range(5) :
        list_of_strings.append(input())
    print(max(list_of_strings))


if __name__ == '__main__' :
    main()