import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called player starting at position row 3,column 2
player = player.Player(3,2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    board.checkMove(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")

    if selection == "w":
        if board.checkMove(player.rowPosition - 1, player.columnPosition) == True:
            player.moveUp()

    elif selection == "s":
        if board.checkMove(player.rowPosition + 1, player.columnPosition) == True:
            player.moveDown()

    elif selection == "a":
        if board.checkMove(player.rowPosition, player.columnPosition - 1) == True:
            player.moveLeft()
     
    elif selection == "d":
        if board.checkMove(player.rowPosition, player.columnPosition + 1) == True:
            player.moveRight()
      
    else: 
        print("Invalid Entry")

    if board.checkWin(player.rowPosition, player.columnPosition) == True:
        print("You Win!")
    break 

    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
