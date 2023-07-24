#import module
from IPython.display import clear_output
import random

# Description : function to display the board
# Author : Mohamed Ahamed VK
# Function Name : displayBoard
# @param : board
def displayBoard(board):

    #clear the output screen
    clear_output()

    #print the board with value
    print(' ','|',' ','|',' ')
    print(board[1],'|',board[2],'|',board[3])
    print(' ','|',' ','|',' ')
    print('-','|','-','|','-')
    print(' ','|',' ','|',' ')
    print(board[4],'|',board[5],'|',board[6])    
    print(' ','|',' ','|',' ')
    print('-','|','-','|','-')
    print(' ','|',' ','|',' ')
    print(board[7],'|',board[8],'|',board[9])        
    print(' ','|',' ','|',' ')

# Description : function to get the user Input
# Author : Mohamed Ahamed VK
# Function Name : playerInput
def playerInput():
    
    #initial Value for marker
    marker = ''
    
    #check the marker value is X or O based on the marker will be set for player
    if not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, choose 'X' or 'O'")
    
    #set the marker to player1 and check it to set the opposite marker for player2
    player1 = marker
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Description : function to place the marker in board
# Author : Mohamed Ahamed VK
# Function Name : playerInput
# @param : board,marker,position
def placeMarker(board,marker,position):

    #override the marker in the board for corresponding position
    board[position] = marker

# Description : function to check the win or not
# Author : Mohamed Ahamed VK
# Function Name : winCheck
# @param : board,marker
def winCheck(board,marker):
    
    #check the row values marks are same     
    row1 = (board[1] == board[2] == board[3] == marker)
    row2 = (board[4] == board[5] == board[6] == marker)
    row3 = (board[7] == board[8] == board[9] == marker)
    #check the column values marks are same
    col1 = (board[1] == board[4] == board[7] == marker)
    col2 = (board[2] == board[5] == board[8] == marker)
    col3 = (board[3] == board[6] == board[9] == marker)
    #check the diagonal values marks are same
    dia1 = (board[1] == board[5] == board[7] == marker)
    dia2 = (board[7] == board[5] == board[3] == marker)

    #return the value based on the condition meet
    return (row1 or row2 or row3 or col1 or col2 or col3 or dia1 or dia2)

# Description : function to decide which user play first
# Author : Mohamed Ahamed VK
# Function Name : chooseFirst
def chooseFirst():

    #using random rand int function to check which player will play first
    flip = random.randint(0,1)

    #check the flip is 0 or not based on the player will play
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# Description : function to check the space is available in board or not
# Author : Mohamed Ahamed VK
# Function Name : spaceCheck
# @param : board,position
def spaceCheck(board,position):

    #return true if the board position is empty space else return false
    return board[position] == ' '

# Description : function to check the board is full or not
# Author : Mohamed Ahamed VK
# Function Name : fullBoardCheck
# @param : board
def fullBoardCheck(board):

    #loop to check is their is a space available in board or not
    for i in range(1,10):

        #check the space in board is their or not
        if spaceCheck(board,i):
            return False
    
    #return true if the board is full
    return True

# Description : function to get the player choice and mapped in the board
# Author : Mohamed Ahamed VK
# Function Name : playerChoice
# @param : board
def playerChoice(board):
    
    #initial Value position
    position = 0
    
    #check the position input and space check for the entered position
    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board,position):
        position = int(input("Chose a position: (1-9)"))

    #return the position value
    return position

# Description : function to check the player want to play again or not
# Author : Mohamed Ahamed VK
# Function Name : replay
def replay():

    #getting input from player to play again or not
    replayChoice = input("Play again Enter Yes or No")
    
    #return true if the replaychoice is Yes
    return replayChoice == 'Yes'

print("*****Welcome to Tic Tac Toe*****")

#loop to game start
while True:

    #initial Board value
    board = [' ']*10    
    #get the marker for player
    player1Marker,player2Marker = playerInput()
    #get the which player play first
    playerTurn = chooseFirst()
    print(playerTurn + " will play first")
    #check the player is ready to play or not
    gameOn = input("Ready to Play Y or N")
    
    #if the player is ready to play then the game will start else game will not start until the player is ready
    if gameOn == "Y":
        playGame = True
    else:
        playGame = False
    
    #gameOn loop
    while playGame:     
        
        #player 1 Turn 
        if playerTurn == 'Player 1':

            #display the board
            displayBoard(board)
            #get the position value from the player 1
            positionValue = playerChoice(board)
            #place the player 1 marker in board
            placeMarker(board,player1Marker,positionValue)

            #check if the player 1 is win or not
            if winCheck(board,player1Marker):

                #display the board and declare as player 1 win
                displayBoard(board)
                print("Player 1 Win")
                #gameOn loop terminate
                playGame = False
            else:

                #check the board is full or not
                #if the board is full then display the board and declare as game tie
                if fullBoardCheck(board):

                    displayBoard(board)
                    print("TIE Game!!")
                else:

                    #player 2 turn enable
                    playerTurn = 'Player 2'
        #player 2 turn
        else:

            #display the board
            displayBoard(board)
            #get the position value from the player 2
            positionValue = playerChoice(board)
            #place the player 1 marker in board
            placeMarker(board,player2Marker,positionValue)
            
            #check if the player 1 is win or not
            if winCheck(board,player2Marker):

                #display the board and declare as player 1 win
                displayBoard(board)
                print("Player 2 Win")
                #gameOn loop terminate
                playGame = False
            else:

                #check the board is full or not
                #if the board is full then display the board and declare as game tie
                if fullBoardCheck(board):

                    displayBoard(board)
                    print("TIE Game!!")
                else:

                    #player 1 turn enable
                    playerTurn = 'Player 1'

    #replay the game or not
    if not replay():
        break

