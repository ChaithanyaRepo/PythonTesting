ItemsCount = 0
if ItemsCount != 1:
    # raise Exception("Cart count not matching")
    pass

assert(ItemsCount == 0)

# AssertionError(ItemsCount ==2)

# try catch mechanism
try:
    with open("fileread.txt", 'r') as reader:
        reader.readlines()
except:
    print("This file is not reachable")

try:
    with open("fileread.txt", 'r') as reader:
        reader.readlines()
except Exception as e:
    print(e)
finally:
    print("Repairing code")
