def factorial(n):

    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n-1)
try:
    print(factorial(1000))
except RuntimeError:
    print("This program calculate factorials that large")
except ZeroDivisionError:
    print("What are doing dividing by zero")
print("Program terminating")