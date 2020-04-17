file = open('fileread.txt', "r")
# print(file)
# reading all the contents of the file
# print(file.read(5))
# print(file.read(-5))
# print(file.readline())
# print(file.readlines())
# file.close()


# Print line ny line using readline method
# line  = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# Reads all the file content and stores in a list
# line = file.readlines()
for line in file.readlines():
    print(line)

# print(line)

file.close()
