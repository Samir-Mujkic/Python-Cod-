location = {0: "you are sitting in front of a computer learning python",
            1: "you are standing at the end of a road before small brick building",
            2: "you are at the top of a hill",
            3: "you are inside a buulding, a wekk house for a small stream",
            4: "you are in a valley beside a stream",
            5: "you are in the forest"}

exits = { 0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = { "QUIR"}

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction + ", "

    print(location)

    if loc == 0:
        break

    direction = input("Available exists are" + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that diretion")