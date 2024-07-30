def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)

        # Get the current player's move
        print("Player", current_player + "'s turn:")
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Please enter a number between 0 and 2.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Make the move
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Check for a winner or a tie
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break
        elif all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()