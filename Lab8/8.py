def main() :
    n, m = map(int, input().split())
    matrix = []
    count = 0
    for i in range(n) :
        matrix.append(list(map(int, input().split())))
    for i in range(1, n - 1) :
        for j in range(1, m - 1) :
            if matrix[i][j] > matrix[i - 1][j] and matrix[i][j] > matrix[i + 1][j] and matrix[i][j] > matrix[i][j - 1] and matrix[i][j] > matrix[i][j + 1] :
                print(matrix[i][j], i + 1, j + 1, sep = ' ')
                count = count + 1
    if count == 0 :
        print(None, n, m, sep = ' ')        
    
    
if __name__ == "__main__" :
    main()