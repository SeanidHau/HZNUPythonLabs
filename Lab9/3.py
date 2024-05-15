def number_to_words(number) :
    output = ""
    num_string = str(number)
    call = {"-": "negative", "0": "zero", "1": "one", "2": "two", "3": "three",
            "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    for num in num_string :
        output += call[num] + " "
    return output
    

def main() :
    num = int(input())
    print(f"{number_to_words(num)}")
            

if __name__ == "__main__" :
    main()