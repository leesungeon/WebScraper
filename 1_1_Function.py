# Function
def say_hello(name="Who"):
    print("Hello,", name)

say_hello("Sungeon")
say_hello()

def sum(a, b):
    return a + b

result_a = sum(3,4)
result_b = sum(5,6)

print(result_a, result_b)

#Keyword Argument
def say_hi(name, age):
    return f"Hello {name} you are {age} years old"

comment = say_hi("eonion", "hi")
print(comment)