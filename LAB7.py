def n_queens(n):
    board = [-1] * n

    def solve(row):
        if row == n:
            for i in range(n):
                print("." * board[i] + "Q" +
                      "." * (n - board[i] - 1))
            return True

        for col in range(n):
            safe = True

            for i in range(row):
                if (board[i] == col or
                    abs(board[i] - col) == abs(i - row)):
                    safe = False
                    break

            if safe:
                board[row] = col
                if solve(row + 1):
                    return True

        return False

    if not solve(0):
        print("No solution exists")


n = int(input("Enter the value of N: "))
n_queens(n)