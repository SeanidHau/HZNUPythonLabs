def main() :
    x, y, z = map(int, input().split())
    if x > z :
        x, z = z, x
    if x > y :
        x, y = y, x
    if y > z :
        y, z = z, y
    print(f"{x}->{y}->{z}")


if __name__ == "__main__" :
    main()