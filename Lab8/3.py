def main() :
    k = int(input())
    ls = list(map(int, input().split()))
    sorted_ls = sorted(ls)
    print(sorted_ls[-k])
    
    
if __name__ == "__main__" :
    main()