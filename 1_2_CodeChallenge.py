def sum(x, y):
    return int(x) + int(y)

def minus(x, y):
    return int(x) - int(y)

def product(x, y):
    return int(x) * int(y)

def power(x, y):
    return int(x) ** int(y)

def quotient(x, y):
    return int(x) / int(y)

def negation(x):
    return -int(x)

def remainder(x, y):
    return int(x) % int(y)


print(sum(3, "7"))
print(minus("9", 1))
print(product(10, 2))
print(power(3, "2"))
print(quotient("9", "4"))
print(remainder("9", "4"))
print(negation("4"))