str0 = "Chaithanya_Nayak"
str1 = "SushmaPrabhu"
str2 = "Sushma"
str3 = "Chaithanya"
print(str0[0])
print(str0[0:10])

print(str0 + str1)

# in keyword used to search for substring
print(str3 in str0)
print(str2 in str1)
print(str2 in str2)

# splitting a string
var = str0.split("_")
print(var)
print(var[0])

# trimming a string
str4 = " ChaithanyaSushma "
print(str4)
print(str4.strip())
print(str4)
print(str4.lstrip())
print(str4.rstrip())
print(str4)
print(str4.capitalize())
print(str4.casefold())
