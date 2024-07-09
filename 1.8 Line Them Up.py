# https://open.kattis.com/problems/lineup

N = int(input())

l = []

for n in range(N):
    l.append(input())

l_sorted = sorted(l)
l_revsorted = sorted(l, reverse=True)

if l == l_sorted:
    print("INCREASING")
elif l == l_revsorted:
    print("DECREASING")
else:
    print("NEITHER")
