t = input("Please enter a text string: ")

text = list(t.lower())

vowels = 0
c_a = text.count("a")
c_e = text.count("e")
c_i = text.count("i")
c_o = text.count("o")
c_u = text.count("u")
print("vowels: ", (c_a + c_e + c_i + c_o + c_u))

vowels_index = []

if c_a != 0:
    vowels_index.append(text.index("a"))
if c_e != 0:
    vowels_index.append(text.index("e"))
if c_i != 0:
    vowels_index.append(text.index("i"))
if c_o != 0:
    vowels_index.append(text.index("o"))
if c_u != 0:
    vowels_index.append(text.index("u"))

vowels_index.sort()

first = 0
if vowels_index.__len__() == 0:
    print("first vowel: no vowel found")
    print("character immediately after first vowel: no vowel found")
else:
    first = vowels_index.pop(0)
    print("first vowel: ", t[first])
    if t.__len__() == first + 1:
        print("character immediately after first vowel: vowel in last position")
    else:
        print("character immediately after first vowel: ", t[first + 1])
