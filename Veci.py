# https://open.kattis.com/problems/veci

##pseudo:
##input X (int)
##konvertera till sträng
##hitta alla permutationer av talets siffror
##lagra dessa i en lista
##bort med dubbletter
##sortera listan efter storlek
##hitta positionen för X i permutations-listan, lagra positionsvärdet
##om X har sista positionen i listan, printa 0, annars printa nästa element

import itertools

def find_integer_permutations(n):
    str_n = str(n)
    permutations = itertools.permutations(str_n)
    permuted_numbers = [int(''.join(p)) for p in permutations]
    cleaned = remove_duplicates(permuted_numbers)
    sorted_permutations = sort_integer_list(cleaned)
    return sorted_permutations

def sort_integer_list(l):
    sorted_list = sorted(l)
    return sorted_list

def remove_duplicates(l):
    return list(set(l))

X = int(input())
permutations = find_integer_permutations(X)

i = 0
while X > permutations[i]:
    i += 1

if X == permutations[len(permutations) - 1]:
    print("0")
else:
    print(permutations[i+1])
