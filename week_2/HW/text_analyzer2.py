word = list(input("Please enter a text string: "))

vowels = {letter: word.count(letter) for letter in ("a", "e", "i", "o", "u")}
print(vowels)