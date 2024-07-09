# https://open.kattis.com/problems/stopwatch

N = int(input())

tider = []
for x in range(N):
    t = int(input())
    tider.append(t)

if N % 2 == 1:
    print("still running")

if N % 2 == 0:
    result = sum([tider[i+1] - tider[i] for i in range(0, len(tider)-1, 2)])
    print(result)
