def main() :
    x, y, z = (int(input()) for _ in range(3))
    print(y * y - 4 * x * z)


if __name__ == "__main__" :
    main()