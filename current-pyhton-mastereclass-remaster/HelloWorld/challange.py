print("please chose")
print("1:tLearn python")
print("2:learn java")
print("3:Go swimming")
print("4:have dinner")
print("5:go to bed")
print("0:eXIT")

while True:
    choice = input()

    if choice  == "0":
       break
    elif choice in "12345":
        print("you chose {}".format(choice))
