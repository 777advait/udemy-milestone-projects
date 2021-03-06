def display_board(board):
	print(' | |')
	print(board[1] + '|' + board[2] + '|' + board[3])
	print(' | |')
	print('-----')
	print(' | |')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print(' | |')
	print('-----')
	print(' | |')
	print(board[7] + '|' + board[8] + '|' + board[9])
	print(' | |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose a marker(X or O):  ').upper()

    if marker == 'X':
        print('Player 1(X) will go first')
        return ('X', 'O')
    else:
        print('Player 2(X) will go first')
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose an index position(1-9):  '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    player = 1
    
    play_game = input('Are you ready to play? Enter Y or N: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        break

    while game_on:
        if player == 1:
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    player = 2

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    player = 1

    if not replay():
        break