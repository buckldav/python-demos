# Make a TicTacToe game

# 2 Player
P1 = "X"
P2 = "O"

# Make a 3x3 array for the grid
n = 3 # Size of grid
grid = [[" " for x in range(n)] for y in range(n)]

# Start of game
currentPlayer = P1
print("Input example:")
print("X: x y = 0 1")
while True:
  # Print out the grid
  print()
  print(grid[0][2] + "|" + grid[1][2] + "|" + grid[2][2])
  print("-+-+-")
  print(grid[0][1] + "|" + grid[1][1] + "|" + grid[2][1])
  print("-+-+-")
  print(grid[0][0] + "|" + grid[1][0] + "|" + grid[2][0])

  # Input
  a = input(currentPlayer + ": x y = ")
  x = int(a.split()[0])
  y = int(a.split()[1])
  # Check if input is within range
  if x < 0 or x >= n or y < 0 or y >= n:
    print("Out of range")
  # Check if square is covered
  elif (grid[x][y] != P1 and grid[x][y] != P2):
    grid[x][y] = currentPlayer
    if currentPlayer == P1:
      currentPlayer = P2
    else:
      currentPlayer = P1
  else:
    print("This square is already covered")
    