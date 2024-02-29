"""TIC TAC TOE | ALPHA-BETA PRUNING"""

# global variables
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')


def is_winner(board, player):
    # checking rows and columns
    for i in range(3):
        if (
            all(cell == player for cell in board[i])
            or
            all(board[j][i] == player for j in range(3))
        ):
            return True

    # checking diagonals
    if (
        all(board[i][i] == player for i in range(3))
        or
        all(board[i][2 - i] == player for i in range(3))
    ):
        return True

    return False


def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def evaluate(board):
    if is_winner(board, PLAYER_X):
        return 10
    elif is_winner(board, PLAYER_O):
        return -10
    elif is_board_full(board):
        return 0
    else:
        return None


def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score is not None:
        return score

    if is_maximizing:
        return maximize(board, depth, alpha, beta)
    else:
        return minimize(board, depth, alpha, beta)


def maximize(board, depth, alpha, beta):
    max_eval = float('-inf')

    for i in range(3):
        for j in range(3):

            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i][j] = EMPTY

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

    return max_eval


def minimize(board, depth, alpha, beta):
    min_eval = float('inf')

    for i in range(3):
        for j in range(3):

            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i][j] = EMPTY

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                if beta <= alpha:
                    break

    return min_eval


def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(
                    board, 0, False, float('-inf'), float('inf')
                )
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


def play_game():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    while True:
        print_board(board)
        player_move = int(input("PLAYER 'O' | Enter your move (1-9): ")) - 1

        if board[player_move // 3][player_move % 3] != EMPTY:
            print("Invalid move. Cell already taken. Try again.")
            continue

        board[player_move // 3][player_move % 3] = PLAYER_O

        if is_winner(board, PLAYER_O):
            print_board(board)
            print("Congratulations! You win!")
            break

        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print("PLAYER 'X' | Computer is thinking...")
        computer_move = find_best_move(board)

        board[computer_move[0]][computer_move[1]] = PLAYER_X

        if is_winner(board, PLAYER_X):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
