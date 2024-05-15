def main() :
    w, x, y, z = map(int, input().split())
    s = set()
    for i in range(w, x + 1) :
        for j in range(y, z + 1) :
            s.add(i / j)
    print(len(s))


if __name__ == "__main__" :
    main()