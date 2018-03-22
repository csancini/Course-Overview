a = input("Please input the number a:")
b = input("Please input the number b:")

numA = float(a)
numB = float(b)

print("The arithmetic mean is: ", round((numA + numB)/2, 2))
print("The geometric mean is: ", round((numA*numB)**0.5, 2))
print("The root-mean-square is: ", round((((numA**2) + (numB**2))/2)**0.5, 2))
