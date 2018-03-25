t = list(input("Please enter a text string: "))

vowels_dic = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

while t.__len__() != 0:
    c = t.pop()
    if c in vowels_dic:
        vowels_dic.update({c: vowels_dic.get(c) + 1})

print(vowels_dic)