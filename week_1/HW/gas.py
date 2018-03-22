typed = input("Please enter the number of gallons of gasoline:")

gallons = float(typed)
liters = gallons * 3.7854
barrels = gallons / 19.5
price = gallons * 3.65

print("The number of gallons entered is ", round(gallons, 2))
print("The equivalent number of liters is ", round(liters, 2))
print("The number of barrels of oil needed to produce it is ", round(barrels, 2))
print("The total price in U.S dollars is ", round(price, 2))