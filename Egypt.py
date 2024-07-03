# https://open.kattis.com/problems/egypt

tripples = []
tripple = ""

k = 0
while tripple != "0 0 0":
    tripple = input()
    tripples.append(tripple)
    k += 1

converted_tripples = []

for tripple in tripples:
    tripple_as_string = tripple.split()
    numbers = [int(num_str) for num_str in tripple_as_string]
    converted_tripples.append(sorted(numbers))

for tripple in converted_tripples:
    if tripple[0] == 0 and tripple[1] == 0 and tripple[2] == 0:
        break
    elif tripple[0]**2 + tripple[1]**2 == tripple[2]**2:
        print("right")
    else:
        print("wrong")
