def main() :
    y, t = map(int, input().split())
    if y < 5 :
        if t <= 40:
            m = 30 * t
        else :
            m = 30 * 40 + 45 * (t - 40)
    else :
        if t <= 40:
            m = 50 * t
        else :
            m = 50 * 40 + 75 * (t - 40)
    print(f"{m:.2f}")


if __name__ == "__main__" :
    main()