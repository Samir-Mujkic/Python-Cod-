locations = {0: "You are sitting in front of a computer learing Python",
             1: "You are standing at the end of a road before a small brick",
             2: "You are at the top of a hill",
             3: "You are inside a buildng a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

#loc = 5
#forest = [locations[exit] for exit in exits if loc in exits[exit].values()]
#print(forest)

##nested comprehension

for loc in sorted(locations):
    exitssss = []
    for xit in exits:
        if loc in exits[xit].values():
            exitssss.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end="\t")
    print(exitssss)

for loc in sorted(locations):
    exitssst = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("location leading {}".format(loc), end="\t")
    print(exitssst)



