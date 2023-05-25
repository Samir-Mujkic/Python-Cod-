low = 1
high = 1000

print("plese think of number betwenn {} and {}".format(low, high))
input("pres enter to start")

guess = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. should i guess higher or lower" "Enter h or l or c if my guess was correcr".format(guess)).casefold()

    if high_low == "h":

        pass
    elif high_low == "l":
        pass

    elif high_low == "c":
        print("i got it in {} guesses!".format(guess))

    else:
        print("please enter h , l or c")
