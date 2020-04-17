# function declaration
def fun(name):
    print("We are inside the function", name)


# function call
# fun()

# Parameterize function call
fun("Chaithanya")


def intsum(a, b):
    print("Summation", a+b)
    return a+b


sumint = intsum(2, 4)
print("Summation", sumint)
