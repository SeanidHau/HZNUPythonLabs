def main() :
    n, m = map(int, input().split())
    image = []
    for i in range(n) :
        image.append(list(map(int, input().split())))

    new_image = [row[:] for row in image]

    for i in range(1, n - 1) :
        for j in range(1, m - 1) :
            ave = round((image[i][j] + image[i - 1][j] + image[i + 1][j] + image[i][j - 1] + image[i][j + 1]) / 5)
            new_image[i][j] = ave
    for row in new_image :
        print(" ".join(map(str, row)))
    
    
if __name__ == "__main__" :
    main()