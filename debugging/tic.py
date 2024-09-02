#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic Tac Toe board.

    Function Description:
    Displays the board in a user-friendly format with rows and columns separated by "|". 
    The rows are separated by a line of dashes.

    Parameters:
    board (list of list of str): A 2D list representing the Tic Tac Toe board, where each element is a string ("X", "O", or " ").

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the Tic Tac Toe board.

    Function Description:
    Determines if any player has won by getting three of their symbols in a row, column, or diagonal.

    Parameters:
    board (list of list of str): A 2D list representing the Tic Tac Toe board, where each element is a string ("X", "O", or " ").

    Returns:
    bool: True if there is a winner, otherwise False.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.

    Function Description:
    Manages the game loop, alternating turns between players "X" and "O". 
    Takes user input for moves and updates the board accordingly. Ends when a player wins.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Check if the input is within the valid range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

    print_board(board)
    # Print the winner. Since the loop ends when there's a winner, it will print the last player who made a move.
    winner = "O" if player == "X" else "X"
    print("Player " + winner + " wins!")

if __name__ == "__main__":
    tic_tac_toe()
