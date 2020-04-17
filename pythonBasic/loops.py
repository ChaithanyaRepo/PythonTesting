greeting = "Good Morning"

if greeting == "Good Morning":
    print("String is  matching")
    print("Second line")
else:
    print("String is not matching")
    print("Else block is executing")

# for loop
values = [2, 3, 4, 5, 6, 7]
for i in values:
    print(i * 2)

# sum of first 5 natural numbers
summation = 0
for j in range(1, 6):
    summation = summation + j
print("summation result")
print(summation)

print("*" * 80)

for k in range(1, 10, 2):
    print(k)
