import random

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(spot != ' ' for spot in board)

# Function for the AI to make a random move
def ai_move(board):
    available_spots = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_spots)

# Main game function
def play_game():
    board = [' '] * 9  # Empty board
    current_player = 'X'  # Human starts as X
    ai_player = 'O'

    while True:
        print_board(board)

        if current_player == 'X':  # Human's turn
            move = int(input("Choose your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Spot taken! Try again.")
                continue
        else:  # AI's turn
            move = ai_move(board)
            print(f"AI chooses spot {move + 1}")

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'  # Switch players

# Start the game
play_game()