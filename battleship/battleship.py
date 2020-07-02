from random import randrange

INIT_CELL = "."
N = 8
grid = [[INIT_CELL for x in range(N)] for y in range(N)]


def printGrid():
    # Print each row
    rowNum = 1
    for row in grid:
        rowPrint = str(rowNum) + " "
        for cell in row:
            rowPrint += cell + " "
        print(rowPrint)
        rowNum += 1
    # Print the row coordinates starting with 'a' in the bottom left
    rowCoordinates = " "
    ASCII = 97
    for i in range(N):
        rowCoordinates += " " + chr(i + ASCII)
    print(rowCoordinates)


def placeShip(BOAT_LENGTH, SHIP_LETTER):
    while True:
        # Decide down or right orientation with random number 0 (DOWN) or 1 (RIGHT)
        direction = randrange(2)
        makeShip = True
        if direction == 0:
            # DOWN
            # Create random coordinates within range
            x = randrange(N)
            # Allow space for the boat downwards
            y = randrange(N - BOAT_LENGTH + 1)
            for j in range(BOAT_LENGTH):
                # Check that spot isn't already taken
                if grid[x][y+j] != INIT_CELL:
                    makeShip = False
                    break
            # Make the ship and break out of the loop if the cells in the grid are available
            if makeShip:
                for j in range(BOAT_LENGTH):
                    grid[x][y+j] = SHIP_LETTER
                break
        else:
            # RIGHT
            # Create random coordinates within range
            # Allow space for the boat to the right
            x = randrange(N - BOAT_LENGTH + 1)
            y = randrange(N)
            for i in range(BOAT_LENGTH):
                # Check that spot isn't already taken
                if grid[x+i][y] != INIT_CELL:
                    makeShip = False
                    break
            # Make the ship and break out of the loop if the cells in the grid are available
            if makeShip:
                for i in range(BOAT_LENGTH):
                    grid[x+i][y] = SHIP_LETTER
                break


def placeShips():
    # Battleship
    placeShip(4, "B")
    # Submarine
    placeShip(3, "S")
    # Cruiser
    placeShip(3, "C")
    # Destroyer
    placeShip(2, "D")


placeShips()
printGrid()
