parrot = "norwegian blue"

letter = input("enter a charachet:")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("i dont need that letter")