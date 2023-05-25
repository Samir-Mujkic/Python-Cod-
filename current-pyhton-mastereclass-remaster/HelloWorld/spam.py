menu = [
    ["eggs", "spam"],
    ["eggs", "bacon", "sausage"],
    ["eggs", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
     if meal[index] == "spam":
        del meal[index]

    print(meal)


samir = [
    ["deba", "MUJKIC"],
    ["SAMIR", "DEBA"],
    ["DEBA", "MUJKIC"],

]

for sam in samir:
    for index in range(len(sam) - 1, -1, -1):
        if sam[index] == "MUJKIC":
            del sam[index]

        print(sam)








