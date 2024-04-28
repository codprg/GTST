#                                                       function
# a function is a block of code which only runs when it is called
# creating a function in a python
"""
        in a python a function is defined using the [def] word 
"""
# -  to call a function use the function name followed by parenthesis


# crate a function
def codprg():
    print("hello codprg")
    # function calling


codprg()


# function arguments/parameter[value add]
def codprg_family(fam):
    print(fam + " family")


codprg_family(input("enter your family "))


# crate a function that add two numbers and return sum
def add(num1, num2):
    print(num1 + num2)


add(45, 34)


def kutr(num1):
    print(f"the user num is: {num1}")


input = input("enter num: ")
kutr(input)
