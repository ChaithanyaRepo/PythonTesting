# file = open('fileread.txt')
#
# file.close()
# Read file and store all line in list
# Reverse the list and write list back to the file

with open('fileread.txt', 'r') as reader:
    content = reader.readlines()
    print(content)
    # for line in reader.readline():
        # print(line)
    # rev_content = reversed(reader.readlines()) # Not able to reverse the content of the file properly
    rev_content = reversed(content)
    print(rev_content)
    with open('fileread.txt', 'w') as writer:
        for line in rev_content:
            print(line)
            writer.write(line)
