name =input("enter you name:")
age =int(input("how old are u, {0}?".format(name)))
print(age)

if age >= 18:
    print("you are old eneguh for vote")
    print("please put an X in the box")
else:
    print("come back in {0} years".format(18 - age))

if age < 18:
    print("please come back in {0} years ".format(18 - age))
else:
    print("you are old eneguh for vote")
    print("please put an X in the box")


