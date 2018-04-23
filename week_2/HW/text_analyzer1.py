# It should then output
# (1) the number of vowels (aeiou)
# (2) the first vowel
# (3) the character immediately after the first vowel.
# Your program should print something helpful (not throw an exception) if the input has no vowels.

# word = input("Please enter a text string: ")

word = "aCrala"
l_word = word.lower()


vowels_count = {n: l_word.count(n) for n in ("a", "e", "i", "o", "u")}
print("vowels:", sum(vowels_count.values()))


vowels_indexes = sorted([l_word.index(k) for k, v in vowels_count.items() if v != 0])
print(vowels_indexes)

if len(vowels_indexes) == 0:
    print("character immediately after first vowel: no vowel found")
else:
    first_vowel_index = vowels_indexes.pop(-1)
    print("first vowel:", word[first_vowel_index])
    if first_vowel_index == len(word)-1:
        print("character immediately after first vowel: vowel in last position")
    else:
        print("character immediately after first vowel: ", word[first_vowel_index + 1])
