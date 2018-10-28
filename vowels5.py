#!/usr/bin/env python3

# This results in a run time error, specifically
# KeyError. This occurs because dictionary keys
# must be initialized.
# This is fixed using the membership opertor(in)
# see vowels6.py

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')
