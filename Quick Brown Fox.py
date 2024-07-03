# https://open.kattis.com/problems/quickbrownfox

import string

alphabet = sorted(set(string.ascii_lowercase))

chars_to_remove = [" ", '.', ',', '?', '!', '’', "'", '"', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

N = int(input())

phrases = []

for n in range(N):
    phrase = input()
    phrases.append(phrase)

def string_cleaner(s, chars):
    for char in chars:
        s = s.replace(char, "").lower()
    s = sorted(set(s))
    return s

cleaned_phrases = [string_cleaner(s, chars_to_remove) for s in phrases]

for phrase in cleaned_phrases:
    if phrase == alphabet:
        print("pangram")
    else:
        letters = []
        nonletters = []
        for char in alphabet:
            if char in phrase:
                letters.append(char)
            else:
                nonletters.append(char)
        missing = ''.join(nonletters)
        print(f"missing {missing}")
