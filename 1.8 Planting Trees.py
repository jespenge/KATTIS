# https://open.kattis.com/problems/plantingtrees

N = int(input())

t = input().split()

t_int = [int(x) for x in t]

t_int_sorted = sorted(t_int, reverse=True)

count_list = []

for i in range(N):
    count_list.append(i+t_int_sorted[i]+2)

print(max(count_list))
