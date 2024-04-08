import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

board = [' ' for _ in range(9)]  # Represents the Tic Tac Toe board

# Create a button list represent 9 buttons on the board
buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                           command=lambda row=row, col=col: on_click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        buttons.append(button)

current_player = 'X'


def on_click(row, col):
    global current_player

    index = row * 3 + col
    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def check_winner():
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return True
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ')
    current_player = 'X'

root.mainloop()
