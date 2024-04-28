"""
                             recursion
 > is the process of defining in terms of itself.
"""

# disadvantage of recursion
# - sometimes the logic behind recursion is hard to follow through
# - calls are expensive [inefficient] as they take up a lot of memory and time
# - function are hard to debug


"""exercise1"""


def gtst(username, age):
    return (
        f"Hello {username},\nYou are {age} years old.\nwere you born in {2024 - age}."
    )


uname = input("Enter your name: ")
uage = int(input("Enter your age: "))
print("====================================")
print(gtst(uname, uage))
