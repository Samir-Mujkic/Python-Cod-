burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]


for meals in [(burger, topping) for burger in burgers for topping in toppings]:
 print(meals)

print()

#for burger in burgers:
 #   for topping in toppings:
   #     print((burger, topping))
#for meals in [[(burger, topping) for burger in burgers] for topping in toppings]
    #print(meals)

times = [(i, i * j) for  i in range (1, 11) for j in range (1, 11)]
print(times)

for x, y in  [(i, i * j) for  i in range (1, 11) for j in range (1, 11)]:
     print(x, y)

