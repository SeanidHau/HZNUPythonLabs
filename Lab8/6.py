def main() :
    numbers = list(map(eval, input().split()))
    mean = sum(numbers) / 10
    square_sum = sum((x - mean) ** 2 for x in numbers)
    deviation = (square_sum / 9) ** 0.5
    print(f"{mean:.2f}", f"{deviation:.2f}", sep = '\n')
    
    
if __name__ == "__main__" :
    main()