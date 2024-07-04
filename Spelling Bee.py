# https://open.kattis.com/problems/spellingbee

##seven_letters = input()
##amount_of_words_in_dictionary = int(input())
##så många inputs
##ta bort alla ord som är färre än 4 bokstäver
##ta bort alla ord som innehåller bokstäver som inte ingår i seven_letters
##ta bort alla ord som inte innehåller första bokstaven i seven_letters
##ord från strippad lista borde nu vara lösningen? printa den listan bara

seven_letters = input()

dictionary_n = int(input())

dictionary = []

for n in range(dictionary_n):
    dictionary_word = input()
    dictionary.append(dictionary_word)

def remove_short_strings(lst):
    return [s for s in lst if len(s) >= 4]

def remove_words_without_seven_letters(lst, letters):
    valid_letters = set(letters)
    return [word for word in lst if all(letter in valid_letters for letter in word)]

def remove_words_without_first_letter(lst, first_letter):
    return [word for word in lst if first_letter in word]

short_dictionary = remove_short_strings(dictionary)
filtered_dictionary = remove_words_without_seven_letters(short_dictionary, seven_letters)

first_letter = seven_letters[0]
final_filtered_dictionary = remove_words_without_first_letter(filtered_dictionary, first_letter)

for word in final_filtered_dictionary:
    print(word)
