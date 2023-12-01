'''
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions
'''
import random

def initialize_board(rows, cols):
    board = []
    for row in range(rows):
        current_row = []
        for col in range(cols):
            current_row.append('*') 
        board.append(current_row)  
    return board

def display_board(board):
    for row in board:
        print(' '.join(row))

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def update_board(board, row, col, player, scores):
    #check the position not have the * and the current player's initial 
    #  it's true then the current player get the point else the player gets place in the board
    if board[row - 1][col - 1] != '*':
        if board[row - 1][col - 1] != player:
            board[row - 1][col - 1] = player
            scores[player] += 1
    else:
        board[row - 1][col - 1] = player

def check_winner(scores):
    #itertate the key and value and score items are display the updated score list
    for player, score in scores.items():
        if score >= 5:
            return player
    return None

def play_game(row,col):
    rows = row
    cols = col
    board = initialize_board(rows, cols)
    scores = {'A': 0, 'B': 0}
    players = ['A', 'B']
    current_player = 0

    while True:
        player = players[current_player]
        #give the message for user to press enter to roll the dice
        input(f"player {player}, press enter to roll the dice ")
        #step: roll the dice
        roll_row, roll_col = roll_dice()
        print(f"player {player} rolled: ({roll_row}, {roll_col})")
        #call the updated_board function then call the display_board function 
        update_board(board, roll_row, roll_col, player, scores)
        display_board(board)
        #print the scores in key and value (dict)
        print(f"player A score: {scores['A']} | player B score: {scores['B']}")
        #check the winner
        winner = check_winner(scores)
        if winner:
            print(f"player {winner} wins!")
            break
        #increament the player, '%' is used to continue the players turns
        current_player = (current_player + 1) % 2

# start the game and give the board size in function call process
play_game(6,6)

