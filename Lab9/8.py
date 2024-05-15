import string

def main() :
    user_input = input().lower()
    dict = {letter: 0 for letter in string.ascii_lowercase}
    for letter in user_input :
        dict[letter] += 1
    for letter, times in dict.items() :
        print(f"{letter}:{times}")
                  

if __name__ == "__main__" :
    main()