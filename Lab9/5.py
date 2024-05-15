def main() :
    dict = {}
    age_list = list(map(int, input().split()))
    for age in age_list :
        if age in dict :
            dict[age] += 1
        else :
            dict[age] = 1
    sorted_dict = sorted(dict.items(), key = lambda item: item[0])
    for age, count in sorted_dict :
        print(f"{age}:{count}")
                   

if __name__ == "__main__" :
    main()