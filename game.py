def print_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return board[i]
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    return None

def play_game():
    board = [" "] * 9
    player = "X"
    winner = None

    while not winner:
        print_board(board)
        move = int(input(f"Player {player}, make your move (1-9): ")) - 1
        if board[move] == " ":
            board[move] = player
            player = "O" if player == "X" else "X"
            winner = check_winner(board)

    print_board(board)
    print(f"Player {winner} wins!")


if __name__ == "__main__":
    play_game()