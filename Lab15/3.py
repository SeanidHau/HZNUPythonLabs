def is_palindrome(str) :
    return str == str[::-1]


def longest_name_in_file() :
    with open("names.txt", "r") as file :
        names = file.readlines()
        
    names = [name.strip() for name in names]
    palindromes = [name for name in names if is_palindrome(name)]
    
    longest_name = max(palindromes, key = len)
    return longest_name
    
    
def main() :
    longest_name = longest_name_in_file()
    print(longest_name)
    
    
if __name__ == "__main__" :
    main()
