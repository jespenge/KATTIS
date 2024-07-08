# https://open.kattis.com/problems/happyprime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_happy_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(char) ** 2 for char in str(n))
    return n == 1

def is_happy_prime(n):
    return is_prime(n) and is_happy_number(n)

def process_datasets(datasets):
    results = []
    for data in datasets:
        set_number, candidate = data
        if is_happy_prime(candidate):
            result = f"{set_number} {candidate} YES"
        else:
            result = f"{set_number} {candidate} NO"
        results.append(result)
    return results

num_datasets = int(input())
datasets = []

for _ in range(num_datasets):
    data_line = input().split()
    set_number = int(data_line[0])
    candidate = int(data_line[1])
    datasets.append((set_number, candidate))

results = process_datasets(datasets)
for result in results:
    print(result)
