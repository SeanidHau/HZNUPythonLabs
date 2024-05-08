def main() :
    numbers = input().split()
    max_number = max(numbers)
    min_number = min(numbers)
    max_index = numbers.index(max_number)
    min_index = numbers.index(min_number)
    print(max_number, max_index, sep = ' ')
    print(min_number, min_index, sep = ' ')
    
    
if __name__ == "__main__" :
    main()