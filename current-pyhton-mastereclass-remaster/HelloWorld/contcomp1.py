menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage" "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meal)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

meals = [meal if "spam" not in meal else " a meal skipped" for meal in menu]

x = 12
expression = "Twelve" if x == 12 else "unknown"
print(expression)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon"if "bacon " in meal else "contains egg")

for x in range(1, 31):
    fizzbuz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuz)

fizzbuz = ["fizz buzz " if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0  else str(x) for x in range(1, 31)]
print(fizzbuz)

for buzz in fizzbuz:
    print(buzz.center(12, "*"))