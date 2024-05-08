def main() :
    n = int(input().strip())
    rule = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    for _ in range(n) :
        DNA_str = input().strip()
        for c in DNA_str :
            print(rule[c], end='')
        print()
        

if __name__ == '__main__' :
    main()