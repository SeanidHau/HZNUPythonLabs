def main() :
    input_string = input().strip()
    while(input_string != '') :
        count = 0
        for char in input_string.lower() :
            if char.isalpha() :
                count += ord(char) - ord('a') + 1
        print(count)
        input_string = input().strip()
        
if __name__ == '__main__' :
    main()