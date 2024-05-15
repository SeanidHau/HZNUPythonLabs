def main() :
    length = int(input())
    user_input = input().lower()
    dict = {}
    for char in user_input :
        if char in dict :
            dict[char] += 1
        else :
            dict[char] = 1
    sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    lst = []
    for i in range(len(sorted_dict)) :
        if sorted_dict[i][1] == sorted_dict[0][1] :
            lst.append(sorted_dict[i][0])
    sorted_lst = sorted(lst)
    print(f"{sorted_lst[0]}")
                  

if __name__ == "__main__" :
    main()