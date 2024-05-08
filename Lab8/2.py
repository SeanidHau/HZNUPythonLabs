def main() :
    n, m = map(int, input().split())
    ls1 = list(map(int, input().split()))
    ls2 = ls1[-m:] + ls1[:-m]
    print(" ".join(map(str, ls2)))
    
    
if __name__ == "__main__" :
    main()