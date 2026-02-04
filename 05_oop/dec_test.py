# functions as variables
def greet():
    print("hi")
# greet() # invoking a function
say_hi = greet # assigining function to a variable
# say_hi() # invoking the variable as function

# function inside another function
def greet1():
    name = input("Enter your name: ")
    def say_hello(n):
        print(f"Hello {n}")
    
    say_hello(name)

# greet1()

def greet2():
    name = input("Enter your name: ")
    return name

def greet3(func):
    print(f"Hello {func()}")

# print(greet2())
# greet3(greet2)

def my_decorator(func):
    def wrapper_function():
        print(f"Hello {func()}")
    return wrapper_function

# print(greet2())
# decorated_greet2 = my_decorator(greet2)
# decorated_greet2()

@my_decorator
def undecorated_function():
    name = input("Enter your name: ")
    return name
# print(undecorated_function())
undecorated_function() # same as calling my_decorator(undecorated_function)

