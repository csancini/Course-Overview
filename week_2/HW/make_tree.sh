#!/usr/bin/env bash
mkdir s1
mkdir s1/s3
mkdir s1/s2
mkdir s1/s2/Advanced

#conf.txt
echo "I love bash scripting." >> s1/s3/conf.txt

#text_analyzer2.py
echo "t = list(input(\"Please enter a text string: \"))" >> s1/s2/Advanced/text_analyzer2.py
echo "" >> s1/s2/Advanced/text_analyzer2.py
echo "vowels_dic = {\"a\": 0, \"e\": 0, \"i\": 0, \"o\": 0, \"u\": 0}" >> s1/s2/Advanced/text_analyzer2.py
echo "" >> s1/s2/Advanced/text_analyzer2.py
echo "while t.__len__() != 0:" >> s1/s2/Advanced/text_analyzer2.py
echo "    c = t.pop()" >> s1/s2/Advanced/text_analyzer2.py
echo "    if c in vowels_dic:" >> s1/s2/Advanced/text_analyzer2.py
echo "        vowels_dic.update({c: vowels_dic.get(c) + 1})" >> s1/s2/Advanced/text_analyzer2.py
echo "" >> s1/s2/Advanced/text_analyzer2.py
echo "print(vowels_dic)" >> s1/s2/Advanced/text_analyzer2.py

#text_analyzer1.py
echo "t = input(\"Please enter a text string: \")" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "text = list(t.lower())" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "vowels = 0" >> s1/s2/text_analyzer1.py
echo "c_a = text.count(\"a\")" >> s1/s2/text_analyzer1.py
echo "c_e = text.count(\"e\")" >> s1/s2/text_analyzer1.py
echo "c_i = text.count(\"i\")" >> s1/s2/text_analyzer1.py
echo "c_o = text.count(\"o\")" >> s1/s2/text_analyzer1.py
echo "c_u = text.count(\"u\")" >> s1/s2/text_analyzer1.py
echo "print(\"vowels: \", (c_a + c_e + c_i + c_o + c_u))" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "vowels_index = []" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "if c_a != 0:" >> s1/s2/text_analyzer1.py
echo "    vowels_index.append(text.index(\"a\"))" >> s1/s2/text_analyzer1.py
echo "if c_e != 0:" >> s1/s2/text_analyzer1.py
echo "    vowels_index.append(text.index(\"e\"))" >> s1/s2/text_analyzer1.py
echo "if c_i != 0:" >> s1/s2/text_analyzer1.py
echo "    vowels_index.append(text.index(\"i\"))" >> s1/s2/text_analyzer1.py
echo "if c_o != 0:" >> s1/s2/text_analyzer1.py
echo "    vowels_index.append(text.index(\"o\"))" >> s1/s2/text_analyzer1.py
echo "if c_u != 0:" >> s1/s2/text_analyzer1.py
echo "    vowels_index.append(text.index(\"u\"))" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "vowels_index.sort()" >> s1/s2/text_analyzer1.py
echo "" >> s1/s2/text_analyzer1.py
echo "first = 0" >> s1/s2/text_analyzer1.py
echo "if vowels_index.__len__() == 0:" >> s1/s2/text_analyzer1.py
echo "    print(\"first vowel: no vowel found\")" >> s1/s2/text_analyzer1.py
echo "    print(\"character immediately after first vowel: no vowel found\")" >> s1/s2/text_analyzer1.py
echo "else:" >> s1/s2/text_analyzer1.py
echo "    first = vowels_index.pop(0)" >> s1/s2/text_analyzer1.py
echo "    print(\"first vowel: \", t[first])" >> s1/s2/text_analyzer1.py
echo "    if t.__len__() == first + 1:" >> s1/s2/text_analyzer1.py
echo "        print(\"character immediately after first vowel: vowel in last position\")" >> s1/s2/text_analyzer1.py
echo "    else:" >> s1/s2/text_analyzer1.py
echo "        print(\"character immediately after first vowel: \", t[first + 1])" >> s1/s2/text_analyzer1.py
