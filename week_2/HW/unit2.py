empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
another_empty_list = list()

weekdays + first_names

list("hello")  # ['h', 'e', 'l', 'l', 'o']


list('cat')

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)

splitme = 'a/b//c/d///e'
splitme.split('/')
splitme.split('//')

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[1]
marxes[-1]
marxes[2] = 'Wanda'
marxes[0:2]
marxes[::2]
marxes[::-2]

# add to the end
marxes.append('Zeppo')

# caution do not use append when combining lists
others = ['Gummo', 'Karl']
marxes.extend(others)
# += works!
marxes += ['A', 'B']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#insert before the offset
marxes.insert(2, 'Gummo')

# delete itens
del marxes[-1]
marxes.remove('Chico')

# remove
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
name1 = marxes.pop()
name2 = marxes.pop(1)
print(marxes)
# append() and pop(0) creates a FIFO

# return the index
idx = marxes.index('Harpo')

#return a boolean
'Groucho' in marxes

marxes.count('Groucho')

# creates a string / combines
joined = ', '.join(marxes)
separated = joined.split(", ")
marxes == separated


marxes = ['Groucho', 'Chico', 'Harpo']
# creates a sorted COPY
new_marxes = sorted(marxes)
# sorts ITSELF
marxes.sort()

# supports different types
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
all_birds[1][0]


numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers.sort(reverse=True)

#number of itens
len(marxes)

# = maintains the reference to the object, copy() replicates
a = [1, 2, 3]
b = a
a[1] = 10
print(b)
c = a.copy()
a[1] = 5
print(a)
print(b)
print(c)

# Tuples, unlike Lists, are immutable and cannot be changed after defined
empty_tuple = ()

# just use comma to separate
one_marx = 'Groucho',
marx_tuple = 'Groucho', 'Chico', 'Harpo'
# the parentheses are optional
marx_tuple = ('Groucho', 'Chico', 'Harpo')

a, b, c = marx_tuple
a
b
c

# exchange statements COOL
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)
