def makeFibonacci(number):
    x = []
    a = 0
    b = 1
    while True:
        c = a+b
        if a < number:
            x.append(a)
            a = b
            b = c
        else:
            return x

print(makeFibonacci(14))
