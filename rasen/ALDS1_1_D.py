n = int(input())
profit = -10**10
minv = 10**10

for i in range(n):
    Ri = int(input())
    profit = max(profit, Ri - minv)
    minv = min(minv, Ri)

print(profit)
