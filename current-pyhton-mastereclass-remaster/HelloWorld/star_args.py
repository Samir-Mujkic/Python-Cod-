def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1, 2, 3, 4))

def build_tuple(*args):
    return args

message_tuple = build_tuple("Hello", "planet", "earth", "take")
print(type(message_tuple))
print(message_tuple)


#-----KVARGS---KVARGS---KVARGS-----

def print_backwards(*args, **kwargs):
    for word in args[::-1]:
        print(word[::-1], end=" ", **kwargs)


with open("backwards.txt", "w") as backwards:
     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards )