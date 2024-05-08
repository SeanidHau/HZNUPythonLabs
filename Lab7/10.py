def prefix(s1, s2) :
    min_lenth = min(len(s1), len(s2))
    common_prefix = []
    for i in range(min_lenth) :
        if s1[i] == s2[i] :
            common_prefix.append(s1[i])
        else :
            return common_prefix
            

def main() :
    s1 = input().strip()
    s2 = input().strip()
    ls = prefix(s1, s2)
    if not ls :
        print("No common prefix")
    else :
        print(''.join(ls))

        
if __name__ == '__main__' :
    main()