def main() :
    nums = input().split()
    s = set()
    ans = []
    for num in nums :
        if num not in s :
            s.add(num)
            ans.append(num)
    for num in ans :
        print(num, end = " ")


if __name__ == "__main__" :
    main()