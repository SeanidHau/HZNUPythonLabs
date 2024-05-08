def main() :
    input_string = input().strip()
    char_count = {}
    for char in input_string :
        if char.isalpha() :
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    for char in sorted(char_count) :
        print(char, ":", char_count[char], sep = '')    


if __name__ == '__main__' :
    main()