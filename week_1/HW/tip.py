typed = input("Enter the price of a meal:")

price = float(typed)

tip = price * 0.16
total = price + tip
print("A 16% tip would be ", round(tip, 2))
print("The total including tip would be ", round(total, 2))