def main() :
    total_people = 45
    for men in range(total_people + 1) :
        for women in range(total_people + 1 - men) :
            children = total_people - men - women
            if men * 3 + women * 2 + children / 2 == 45 :
                print(men, women, children, sep = ' ')


if __name__ == "__main__" :
    main()