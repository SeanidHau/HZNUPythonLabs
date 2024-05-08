def check(n, chess_board) :
    for i in range(n) :
        if all(chess_board[i][0] == chess_board[i][j] for j in range(n)) :
            return 'X' if chess_board[i][0] == 1 else 'O'
        if all(chess_board[0][i] == chess_board[j][i] for j in range(n)) :
            return 'X' if chess_board[0][i] == 1 else 'O'
    if all(chess_board[0][0] == chess_board[i][i] for i in range(n)) :
        return 'X' if chess_board[0][0] == 1 else 'O'
    if all(chess_board[0][n - 1] == chess_board[i][n - i - 1] for i in range(n)) :
        return 'X' if chess_board[0][n - 1] == 1 else 'O'
    return 'NIL'


def main() :
    n = int(input())
    chess_board = []
    for _ in range(n) :
        chess_board.append(list(map(int, input().split())))
    print(check(n, chess_board))
        
    
if __name__ == "__main__" :
    main()