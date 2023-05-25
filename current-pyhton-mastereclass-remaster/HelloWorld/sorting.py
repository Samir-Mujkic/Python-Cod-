pangram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.5, 5.5]
samira = sorted(numbers)
print(samira)

samir = sorted("samir je paMatan", key=str.casefold)
print(samir)

deba = ["grahama",
        "samir",
        "John",
        "Eric",
        "Samir",
        ]
deba.sort(key=str.casefold)
print(deba)