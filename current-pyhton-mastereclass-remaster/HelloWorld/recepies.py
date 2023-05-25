import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tim of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup
    recipes["bit"].append("butter")
    recipes["pasta"].append("tomato")
    for snack in recipes:
        print(snack, recipes[snack])