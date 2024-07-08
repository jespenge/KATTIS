# https://open.kattis.com/problems/goldbach2

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

def goldbach_conjecture(even_integer):
    if even_integer <= 2 or even_integer % 2 != 0:
        print(f"{even_integer} is not a valid even integer greater than 2.")
        return
    
    representations = []
    for num1 in range(2, even_integer // 2 + 1):
        if is_prime(num1):
            num2 = even_integer - num1
            if is_prime(num2):
                representation = f"{num1}+{num2}"
                representations.append(representation)
    
    if not representations:
        print(f"{even_integer} has no valid representations according to Goldbach's conjecture.")
    else:
        print(f"{even_integer} has {len(representations)} representation(s)")
        for representation in representations:
            print(representation)

num_tests = int(input())
test_integers = []
for _ in range(num_tests):
    test_int = int(input())
    test_integers.append(test_int)

for integer in test_integers:
    goldbach_conjecture(integer)
    print()
