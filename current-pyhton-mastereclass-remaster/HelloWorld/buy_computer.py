current_choice = "-"
computer_parts = []
while current_choice != "0":
    if current_choice in "12345":
        print("adding {}".format(current_choice))    else:
        print("please add options from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("0: to finish")
    current_choice = input()

