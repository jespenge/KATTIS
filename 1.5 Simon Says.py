# https://open.kattis.com/problems/simonsays

N = int(input())

inputs = []

for i in range(N):
    user_input = input()
    inputs.append(user_input)

filtered_strings = [s for s in inputs if s.startswith("Simon says")]

modified_strings = [s.replace("Simon says", "", 1).strip() for s in filtered_strings]

for s in modified_strings:
    print(s)
