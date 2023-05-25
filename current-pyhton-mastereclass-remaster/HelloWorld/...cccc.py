def fizz_buzz(number: int) ->str:


    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return  "fizz"
    elif number % 5 == 0:
        return  "buzz"
    else:
        return str(number)

input("play fizz buzz. press enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("your go : ")
    if players_answer != correct_answer:
        print("you lose, the correcet answer was {}".format(correct_answer))
        break
else:
    print("well done you reach {}".format(next_number))

