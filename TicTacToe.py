#Name: Yzer De Gula
#Email: YZER.DEGULA25@myhunter.cuny.edu
#Date: 03/26/2022
#This program allow 2 players to play a game of tic tac toe

import random

#Has 10 elements so that we start at 1 and can correlate to the numpad
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_board2 = ['#','X','O','X','O','X','O','X','O','X']


def display_board(board):
    print('        |       |       ')
    print(f'    {board[7]}   |   {board[8]}   |   {board[9]}   ') 
    print("--------|-------|--------")
    print(f'    {board[4]}   |   {board[5]}   |   {board[6]}   ')
    print("--------|-------|--------")
    print(f'    {board[1]}   |   {board[2]}   |   {board[3]}   ')
    print('        |       |       ')

#display_board(test_board)

def player_input():
    marker = ""

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_input()

def position():
    position = ""

    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("Choose your next position: (1-9)")

        if position not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry, that is not a valid choice. Please choose a position from (1-9)")

    return int(position)

def place_marker(board,marker,position):
    #Given the position replace that index on the board with the marker
    board[position] = marker


#place_marker(test_board,player_input(),position())
#display_board(test_board)


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return "Player 1 Goes First"
    else:
        return "Player 2 Goes First"

#print(choose_first())

def space_check(board,position):
    return board[position] == " "

#print(space_check(test_board,2))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#print(full_board_check(test_board))
#print(full_board_check(test_board2))

def player_choice(board):
    pos = 0

    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
        pos = int(input("Choose your next position: (1-9) "))
    return pos

#print(player_choice(test_board))

def replay():
    ans = ""

    while ans not in ['Y','N']:
        ans = input("Would You Like to Play Again (Y/N)?")

        if ans not in ['Y','N']:
            print("Sorry, that is not a valid choice. \n Please Answer (Y/N):")

    if ans == 'Y':
        return True
    elif ans == 'N':
        return False

#print(replay())

###     F I N A L         G A M E    ####

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? (Y/N).')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

