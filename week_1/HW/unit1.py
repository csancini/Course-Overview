
# basics
a = 7
print(a)
type(a)
type(67.4)
type('bc')
b = 5 + 8
print(3/7)
print(7//3)
print(7%3)
print(3**4)
b -= 2

int(True)
int(False)
int('92')
float(98)
float('-1.0e4')

# the first command cannot be used, and the second is a work around
int('5.5')
int(float('5.5'))

# floating number rounding error (number as store in base 2 and there are precision problems
0.1 + 0.1 + 0.1 == 0.3


# return both the quotient and the remainder
print(divmod(9, 5))

print(type(divmod(9, 5)))
print(type(7))

# python let the type be changed
x = 1
print(type(x))
x = 'a'
print(type(x))

# Strings
# both use of ' and "  for strings
print("'Nay,' said the naysayer.")
print('"Nay," said the naysayer.')

print(99, 'bottles', 'would be enough.')
palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

s = 'Release the kraken! ' \
    + 'At once!'

#combine with + and duplicate with *
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# Slices, Split, Join

#offset em 0
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)
letters[:]

# from offset 4 to 19, by 3
print(letters[4:20:3])
# last 3
letters[-3:]

# when used in the end removes 3 characters
letters[18:-3]

# step backwards
print(letters[::-1])
print(len(letters))

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos)
f = todos.split(',')
print(f)
j = ' # '.join(f)
print(j)

# Playing with Strings
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
word = 'the'
print(
    poem[:13],
    len(poem),
    poem.startswith('All'),
    poem.endswith('That\'s all, folks!'),
    poem.find(word),
    poem.rfind(word),
    poem.count(word),
    poem.isalnum())

setup = 'a Duck goes into a bar...'
setup.strip('.')
setup.capitalize()
setup.title()
setup.upper()
setup.lower()
setup.swapcase()

# center with 30 characters
setup.center(30)

setup.ljust(30)


setup.replace('Duck', 'Marmoset')
setup.replace('a ', 'a famous ', 100)