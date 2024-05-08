def main() :
    numbers = list(map(int, input().split()))
    odd_part = sorted(num for num in numbers if num % 2 == 1)
    even_part = sorted(num for num in numbers if num % 2 == 0)
    sorted_nums = odd_part + even_part
    print(" ".join(map(str, sorted_nums)))
    
    
if __name__ == "__main__" :
    main()