# functions as variables

def greet1():
    print("hi")

say_hello = greet1

# say_hello()

# function inside function

def greet2():
    def get_name():
        return input("Enter your name: ")
    print(f"Hello {get_name()}")

# greet2()

# function that accepts another function

def greet3(func):
    def wrapper():
        name = input("Enter your name: ") 
        func()
        print(name)
    return wrapper

# greet4 = greet3(greet1)
# greet4()

@greet3
def greet4():
    print("Hi.....", end = " ")

greet4()