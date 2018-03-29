accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

for card in accusation:
    print(card)

print("")

for value in accusation.values():
    print(value)

print("")

for item in accusation.items():
    print(item[0], item[1])

print("")

for key, value in accusation.items():
    print(key, value)

print("")

for x in range(5, -1, -1):
    for j in range(x + 1):
        print(j, end=" ")
    print("")

print("")

# list comprehensions
number_list = [number for number in range(1, 6)]
print(number_list)

print("")

number_list = [number for number in range(1, 6) if number % 2 == 1]
print(number_list)

print("")
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

print("")
cells = [(row, col) for row in rows for col in cols]
print(cells)  # list of tuples
print("")
for cell in cells:
    print(cell)

# Dictionary Comprehensions
print("")
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

print("")
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# Set Comprehensions
print("")
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)


# Generator Comprehensions
# Tuples do not have comprehensions
# Using parentheses creates a generator comprehension
print("")
number_thing = (number for number in range(1, 6))
print(type(number_thing))

# A generator can be run only once. Lists, sets, strings, and dictionaries
# exist in memory, but a generator creates its values on the fly and
# hands them out one at a time through an iterator. It doesn?t remember
# them, so you can?t restart or back up a generator.
print(list(number_thing))
print(list(number_thing))