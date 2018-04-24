def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())


def menu1(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def menu2(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


# problem
def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')


# problem fixed
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')
nonbuggy('b')


# grouped parameters in a tuple
def print_args(*args):
    print('Positional argument tuple:', args)


print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


# grouped parameters in a dictionary
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# docstring
def print_if_true(thing, check):
    """
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    """
    if check:
        print(thing)


help(print_if_true)
print(print_if_true.__doc__)


# functions as arguments
def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)


# combine this with the *args and **kwargs
# You can use functions as elements of lists, tuples, sets, and dictionaries.
# Functions are immutable, so you can also use them as dictionary keys.
def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))


# inner functions
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'))


# Closures
# An inner function can act as a closure. This is a function that is dynamically generated
# by another function and can both change and remember the values of variables that
# were created outside the function.
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a())
print(b())


# lambda function
def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):
    return word.capitalize() + '!'


stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')


# generator functions
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


ranger = my_range(1, 5)
print(ranger)
for i in ranger:
    print(i)

def print_args(*args, **kwargs):
    print(args)
    print(kwargs)


print_args('ops','abc', 3, 5, arg1='ops')
print_args(2, arg1='ops', arg2='abc', arg3=3, arg4=5)


def answer():
    print(42)


def run_something(func):
    func()


run_something(answer)


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 1, 2)


# A decorator is a function that takes one function as input and returns another function
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b


add_ints(3, 5)

cooler_add_ints = document_it(add_ints) # manual decorator assignment
cooler_add_ints(3, 5)

print("")


@document_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)