# Variables
START_X = 0 # TODO
START_Y = 0 # TODO
MAP_X = 4   # TODO
MAP_Y = 8   # TODO

x = START_X
y = START_Y

# Commands
def go(direction):
    global x 
    global y 
    if direction == 'north':
        if (y + 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y += 1
            print("Went north")
    # TODO: elif, add the other directions
    else:
        print("I don't understand which direction you're trying to go")

# Game loop
while True:
    # Print out all the stuff related to the room
    print("Position x: " + str(x))
    print("Position y: " + str(y))

    # Get input from the user
    fromUser = input()
    if fromUser == "quit":
        print("Game over!")
        break
    elif fromUser.split()[0] == "go":
        go(fromUser.split()[1])
    else:
        print("That didn't make any sense to me")