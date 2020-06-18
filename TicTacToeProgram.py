#from IPython.display import clear_output
import random

def display_board(board):
    #clear_output()
    print('   |     | ')
    print(board[7],' | ', board[8], ' | ', board[9])
    print('   |     | ')
    print('--------------')
    print('   |     | ')
    print(board[4], ' | ', board[5], ' | ', board[6])
    print('   |     | ')
    print('--------------')
    print('   |     | ')
    print(board[1], ' | ', board[2], ' | ', board[3])
    print('   |     | ')

def player_input():
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1 please choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or # top straight across
           (board[4] == mark and board[5] == mark and board[6] == mark) or # middle straight across
           (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom straight across 
           (board[7] == mark and board[4] == mark and board[1] == mark) or # left  straight down
           (board[8] == mark and board[5] == mark and board[2] == mark) or # middle straight down
           (board[9] == mark and board[6] == mark and board[3] == mark) or # right straight down 
           (board[1] == mark and board[5] == mark and board[9] == mark) or # diagnol across
           (board[3] == mark and board[5] == mark and board[7] == mark)) # diagnol across

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Please enter your next position 1-9: '))
    
    return position

def replay():
    return input('Would you like to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Are you ready to play? Please enter Y or N: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            #player 1's turn 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print(' Congratulations you have won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print(' It is a draw!')
                    break
                else:
                    turn = 'Player 2'
            
            
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print(' Congratulations you have won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print(' It is a draw!')
                    break
                else:
                    turn = 'Player 1'
                
                
                
    if not replay():
        break
