import random

def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]

    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != ' ':
            return board[win[0]]

    if ' ' not in board:
        return 'Tie'

    return None

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        display_board(board)
        if current_player == 'X':
            print("Player", current_player + "'s turn")
            move = int(input("Please enter the position (0-8) where you want to place your mark: "))
            if board[move] != ' ':
                print("That position is already taken. Please choose another position.")
                continue
        else:
            print("Computer's turn")
            available_moves = [i for i, x in enumerate(board) if x == ' ']
            move = random.choice(available_moves)

        board[move] = current_player

        winner = check_win(board)
        if winner:
            display_board(board)
            if winner == 'Tie':
                print("The game ends in a tie.")
            else:
                print("Player", winner, "wins!")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play_game()
