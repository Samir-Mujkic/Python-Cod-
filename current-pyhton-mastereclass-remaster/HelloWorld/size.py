import sys

def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_Range is returning {}".format(start))
        yield  start
        start += 1
#_ = input("line 12")
#big_range = range(10000)
big_range = range(5)
#_ = input("line 15")

#print(next(big_range))
print("big range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []
#_ = input("line 22")
for val in big_range:
    big_list.append(val)

print("big list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
for i in my_range(5):
    print("i is {}".format(i))
