# Step 1: Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Display the game board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Step 3: Handle player input
def get_move():
    while True:
        move = input("Enter your move (row[1-3], column[1-3]): ")
        try:
            row, col = map(int, move.split(','))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Step 4: Check for a win
def check_win(player):
    for i in range(3):
        if board[i] == [player] * 3:
            return True
        if [board[j][i] for j in range(3)] == [player] * 3:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Step 5: Main game loop
current_player = 'X'
while True:
    display_board(board)
    print("Player", current_player)
    row, col = get_move()
    board[row][col] = current_player
    if check_win(current_player):
        display_board(board)
        print("Player", current_player, "wins!")
        break
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        display_board(board)
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
