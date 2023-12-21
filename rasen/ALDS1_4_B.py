n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
C = 0

for i in T:
    f = 0
    l = len(S)-1
    while f <= l :
        mid = (f+l)//2
        if i < S[mid]:
            l = mid-1
        elif i > S[mid]:
            f = mid+1
        else:
            C += 1
            break
print(C)
