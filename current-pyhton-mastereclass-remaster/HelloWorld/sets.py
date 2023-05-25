farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("-" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horese")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)
even = set(range(0, 40, 2))
print(even)


squares_tuple = (4, 6, 16,)
squares = set(squares_tuple)
print(squares)
evenss = (0, 100, 2,)
evens = frozenset(evenss)

print(evens)



#print(sorted(even.symmetric_difference(squares)))
#print(sorted(squares.symmetric_difference(even)))