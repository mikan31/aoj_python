def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j] < C[j-1]:
                C[j],C[j-1] = C[j-1],C[j]

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
