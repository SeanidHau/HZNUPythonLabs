def mean_mediant(t) :
    sorted_t = sorted(t)
    n = len(t)
    mid = 0
    if n % 2 == 1 :
        mid = sorted_t[n // 2]
    else :
        mid = (sorted_t[n // 2] + sorted_t[n // 2 - 1]) / 2
    ave = sum(t) / n
    return ave, mid
        

def main() :
    numbers = tuple(map(int, input().split()))
    ave_num, mid_num = mean_mediant(numbers)
    print(f"({ave_num}, {mid_num})")
    
    
if __name__ == "__main__" :
    main()