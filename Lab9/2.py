def main() :
    count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    vowels = "aeiou"
    user_input = input().lower()
    for char in user_input :
        if char in vowels :
            count[char] += 1
    for vowels, times in count.items() :
        print(f"{times}", end = ' ')
            

if __name__ == "__main__" :
    main()