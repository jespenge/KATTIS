# https://open.kattis.com/problems/transitwoes

s, t, n = map(int, input().split())
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(0, n):
    s += d[i]
    if s % c[i] != 0:           #om han behöver vänta på bussen
        s += c[i] - (s % c[i])  #så väntar han så här många minuter på den
    s += b[i]
s += d[n]
if s <= t:
    print("yes")
else:
    print("no")
