def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def tic_tac_toe():
    board = [str(i + 1) for i in range(9)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Try again.")
                continue

            if board[move] in ["X", "O"]:
                print("Position already taken! Try again.")
                continue

            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if all(cell in ["X", "O"] for cell in board):
                print_board(board)
                print("🤝 It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a number between 1 and 9.")


tic_tac_toe()