import shelve

fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet,orange,citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow citrus fruit"
fruit["grape"] = "a small,sweat fruit growing in bunces"
fruit["line"] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit["line"] = "great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])

fruit.close()

print(fruit)