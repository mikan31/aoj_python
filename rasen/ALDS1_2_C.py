def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(C1, C2, N):
    if C1 != C2: return False
    return True

N = int(input())
C = list(input().split())
C1 = C.copy()
C2 = C.copy()
C1 = BubbleSort(C1, N)
print(" ".join(C1))
print("Stable")
C2 = SelectionSort(C2, N)
print(" ".join(C2))
if isStable(C1, C2, N):
    print("Stable")
else:
    print("Not stable")
