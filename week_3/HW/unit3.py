empty_dict = {}

bierce = {'misfortune': 'The kind of fortune that never misses',
          'positive': "Mistaken at the top of one's voice",
          'day': 'A period of twenty-four hours, mostly misspent'}
print(bierce)

# any sequence containing two-item sequences
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

pythons = dict(Cleese='John', Jones='Terry', Palin='Michael', Chapman='Graham', Idle='Eric')
pythons['Gilliam'] = 'Gerry'
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

del pythons['Marx']

pythons.clear()
pythons = {}

pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael'}
'Chapman' in pythons

pythons['Cleese']

# throws exception if the key is not present, but not with get
#pythons['Marx']

pythons.get('Cleese')
pythons.get('Marx') == None

pythons.keys()
pythons.values()
pythons.items()

# copy
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confise everyne'
print(save_signals)

new_signals = save_signals.copy()
save_signals['black'] = 'surprise'
print(new_signals)
print(save_signals)

#set
empty_set = set()
set(['Dasher', 'Dasher', 'Prancer', 'Mason-Dixon'])
set(('Ummagumma', 'Ummagumma', 'Atom Heart Mother'))

# form dicts only takes keys
set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )

set("letters")

even_numbers = {0, 2, 4, 6, 8}

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print("")

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# uso de operadores logicos
print("")
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

print("")
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print("")
print(drinks['black russian'])

# mais operadores logicos
a = {1, 2}
b = {2, 3}
bruss = drinks['black russian']
wruss = drinks['white russian']


a & b
a.intersection(b)

a | b
a.union(b)

a - b
a.difference(b)

a ^ b
a.symmetric_difference(b)  # items in one set or the other, but not both

a <= b
a.issubset(b)
a <= a
a.issubset(a)

# To be a proper subset, the second set needs to have all the members of the first and more
a < b
bruss < wruss

# Python?s comparison operators are:
# equality              ==
# inequality            !=
# less than             <
# less than or equal    <=
# greater than          >
# greater than or equal >=
# membership            in

# boolean operators
x = 7
5 < x and x < 10
(5 < x) and (x < 10)
5 < x and x > 10
5 < x and not x > 10

# A false value doesn't necessarily need to explicitly be False.
# For example, these are all considered False:

# boolean         False
# null            None
# zero integer    0
# zero float      0.0
# empty string    ''
# empty list      []
# empty tuple     ()
# empty dict      {}
# empty set       set()

some_list = [1]
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

# If the while loop ended normally (no break call), control passes to an optional else.
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:  # break not called
    print('No even number found')

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