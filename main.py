#TIC-TAC-TOE AI

import random

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print("|")
    print("---------")

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Check for a tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "Tie"
    # No winner yet
    return None

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner is not None:
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        else:
            return 0

    if maximizing_player:
        max_eval = float("-inf")
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "X"
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "O"
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = float("-inf")
    best_move = None
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = "X"
        eval = minimax(board, 0, False)
        board[cell[0]][cell[1]] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = cell
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        print("AI is thinking...")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "X"
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

play_game()

