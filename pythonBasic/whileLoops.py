it = 10

while it > 1:
    if it == 3:
        break
    if it == 4:
        it = it - 1
        continue
    print(it)
    it = it - 1


print("Loop terminated")