import random as rand

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))

    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("The spot is taken! Choose another spot.")

# Check for horizontal win
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

# Check for vertical win
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

# Check for diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

# Check for tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        global gameRunning
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Check for win
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        global gameRunning
        gameRunning = False

# Computer move
def computer(board):
    if currentPlayer == "O":
        while True:
            position = rand.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                break

# Main game loop
while gameRunning:
    printBoard(board)
    if currentPlayer == "X":
        playerInput(board)
    else:
        computer(board)
    checkWin()
    if not gameRunning:
        break
    checkTie(board)
    if not gameRunning:
        break
    switchPlayer()