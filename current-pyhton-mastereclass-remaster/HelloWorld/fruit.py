fruit = {"orange": "a sweat, orange, citrus fruit",
         "apple": "a good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "can i habe some more fruit, please"}

print(veg)

veg.update(fruit)
print(veg)

print(fruit.update(veg))
print(fruit)

nice_and_nast =fruit.copy()
nice_and_nast.update(veg)
print(nice_and_nast)