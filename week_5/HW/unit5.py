import sys
from collections import defaultdict
from collections import Counter
from collections import OrderedDict

for place in sys.path:
    print(place)


periodic_table = defaultdict(int)
periodic_table.update({"Hydrogen": 1, "Helium": 2})
print(periodic_table["Hydrogen"])

# adds an element with the specified value if not present
print(periodic_table.setdefault("Carbon", 12))
print(periodic_table.setdefault("Hydrogen", 12))

# default value created by defaultdict
print(periodic_table["Lead"])

bestiary = defaultdict(lambda: "Huh?")
print(bestiary["E"])

# Using int is one way to make your own counter:
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# count using Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())   # all elements in order
print(breakfast_counter.most_common(1))  # first
print(breakfast_counter.most_common(2))  # first and second

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

# union of counters
print(lunch_counter + breakfast_counter)

# OrderedDict
quotes = OrderedDict((
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')))

for stooge in quotes:
    print(stooge)
