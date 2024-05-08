def main() :
    y, m, d = map(int, input().split())
    if m < 3 :
        m = 12 + m
        y -= 1
    h = (d + int(26 * (m + 1) / 10) + y % 100 + int((y % 100) / 4) + int(int(y / 100) / 4) + 5 * int(y / 100)) % 7
    if h == 2 :
        print("Monday")
    elif h == 3 :
        print("Tuesday")
    elif h == 4 :
        print("Wednesday")
    elif h == 5 :
        print("Thursday")
    elif h == 6 :
        print("Friday")
    elif h == 0:
        print("Saturday")
    elif h == 1 :
        print("Sunday")


if __name__ == "__main__" :
    main()