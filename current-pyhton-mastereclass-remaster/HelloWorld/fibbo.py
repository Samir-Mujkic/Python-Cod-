def fibbonacci(n):

    if 0 <= n <= 1:
        return n

    samir, deba = 1, 0


    result=None
    for f in range(n-1):
        result = deba + samir
        deba = samir
        samir = result

    return result

for i in range (15):
    print(i, fibbonacci(i))
