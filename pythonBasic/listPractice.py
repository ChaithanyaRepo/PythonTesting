values = [1, 2, 3, "sushma", "chaithanya"]

print(values[0])
print(values[4])
print(values[3])
print(values[2:4])

values.insert(5, "sony")

print(values)
values.append("ammi")

values[5] = "Ammi"
print(values)

del values[6]
print(values)

val = (1, 2, "jaanu", "ammi")

store = {'1': "Chaithanya", 2: "Sushma"}
print(store['1'])

dict = {}
dict["Firstname"] = "Chaithanya"
dict["Lastname"] = "Sushma"

print(dict)

dict["Fullname"] = "ChaiSush"
print(dict)