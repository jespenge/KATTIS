# https://open.kattis.com/problems/numberfun

N = int(input())

l = []

for n in range(N):
    tretal_str = input()
    tretal_splittad = tretal_str.split()
    a = int(tretal_splittad[0])
    b = int(tretal_splittad[1])
    c = int(tretal_splittad[2])
    if a + b == c or a - b == c or b - a == c or a*b == c or a/b == c or b/a == c:
        l.append("Possible")
    else:
        l.append("Impossible")

for n in l:
    print(n)
