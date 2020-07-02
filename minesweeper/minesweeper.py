from random import randrange

MINE = "*"
N = 8
INIT_CELL = "."
grid = [[INIT_CELL for x in range(N)] for y in range(N)]


def printGrid():
    for row in grid:
        rowPrint = ""
        for cell in row:
            rowPrint += cell + " "
        print(rowPrint)


def initializeMines(number):
    for i in range(number):
        minePlaced = False
        while minePlaced == False:
            x = randrange(N)
            y = randrange(N)
            if grid[x][y] == INIT_CELL:
                grid[x][y] = MINE
                minePlaced = True


def calculateMineNeighbors():
    for i in range(N):
        for j in range(N):
            gridNumber = 0
            if grid[i][j] != MINE:
                # Check all the cells around the current cell (including diagonal neighbors)
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i+k >= 0 and j+l >= 0 and i+k < N and j+l < N:
                            if grid[i+k][j+l] == MINE:
                                gridNumber += 1
            if gridNumber != 0:
                grid[i][j] = str(gridNumber)


initializeMines(12)
calculateMineNeighbors()
printGrid()
