fruit = {"orange": " a sweet, organge, citrus firut",
         "apple": " good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
while True:
    dict_key = input("plaase enter a fruit: ")
    if dict_key == "quit":
        break
    #if dict_key in fruit:
    # descritpion = fruit(dict_key)
     #   print(description)
    else:
        print("we dont have" + dict_key)