def main() :
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l3 = l1 + l2
    s1 = set(l1)
    s2 = set(l2)
    ans = sorted(list(s1 ^ s2), key = l3.index)
    for i in range(len(ans) - 1) :
        print(ans[i], end = " ")
    print(ans[len(ans) - 1])

    


if __name__ == "__main__" :
    main()