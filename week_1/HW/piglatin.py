name = input("Please enter your name:")

output = ""
for i, val in enumerate(name.split(" ")):
    output += (val[1:] + val[0] + "ay").capitalize() + " "

print(output[:-1])
