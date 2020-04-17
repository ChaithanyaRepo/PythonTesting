var = "Good"
val = None


def varUpdate():
    global var
    print(var)
    var = "Good Morning"
    valUpdate(1)


def valUpdate(val1):
    global val
    val = val1
    print(val)

