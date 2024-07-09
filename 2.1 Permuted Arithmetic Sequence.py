# https://open.kattis.com/problems/permutedarithmeticsequence

def is_arithmetic_sequence(sequence):
    d = sequence[2] - sequence[1]
    for i in range(1, len(sequence) - 1):
        if sequence[i+1] - sequence[i] != d:
            return False
    return True

def can_be_arithmetic_sequence(sequence):
    first_element = sequence[0]
    remaining_sequence = sequence[1:]
    sorted_sequence = [first_element] + sorted(remaining_sequence)
    d = sorted_sequence[2] - sorted_sequence[1]
    for i in range(1, len(sorted_sequence) - 1):
        if sorted_sequence[i + 1] - sorted_sequence[i] != d:
            return False
    return True

n = int(input())
sequences = []

for i in range(n):
    sequence = input()
    sequence_as_strings = sequence.split()
    sequence = [int(x) for x in sequence_as_strings]
    sequences.append(sequence)

for sequence in sequences:
    if is_arithmetic_sequence(sequence):
        print("arithmetic")
    elif can_be_arithmetic_sequence(sequence):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
