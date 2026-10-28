def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")


def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move(board):
    best_score = float("-inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"


def play_game():
    board = [" "] * 9

    print("TIC-TAC-TOE")
    print("Positions are numbered 1 to 9:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        # Human move
        try:
            pos = int(input("\nEnter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid position! Try again.")
            continue

        board[pos] = "X"
        print("\nCurrent board:")
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break

        if " " not in board:
            print("It's a draw!")
            break

        # Computer move
        computer_move(board)
        print("\nComputer's move:")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if " " not in board:
            print("It's a draw!")
            break


play_game()
