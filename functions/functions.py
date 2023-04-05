# functions

# Allow you to follow DRY

# Do Not Repeat Yourself

# def print_something():
#     print("something has been printed")
#
# print_something()
# print_something()
# print_something()
# print_something()

def print_something(print_string):
    print(print_string)

print_something("My name is Luke")
print_something("My second name is Fairbrass")

# def greeting(name):
#     print("Hello, my name is " + name)
#
# greeting("Luke")
# greeting("Fatima")

# return statement

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguements

def addition(int1=2, int2=2):
    return int1 + int2

print(addition(10, 2))

# multiple arguements
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 2)

# Type hints

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(24601)

def division(denum: int, num: int) -> float:
    return denum / num

print(type(division(12, 5)))

# this function subtracts two numbers
def subtraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2

print(type(subtraction()))

# functions best practices

# 1. Name your methods using lowercase and underscores
# 2. All arguements should be clear in their need and where possible their expected type
# 3. remember the return statement or your function will return None in most cases
# 4. Keep your functions as small as possible, and keep them readable
# 5. Use comments within your methods to help with instructions on how to use them
# 6. Consider using Type Hints to avoid errors earlier









