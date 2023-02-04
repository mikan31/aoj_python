n = int(input())
l = list(map(int, input().split()))

l.reverse()
print(" ".join([str(n) for n in l]))
