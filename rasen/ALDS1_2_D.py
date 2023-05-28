
def insertionSort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1

def shellSort(A, n):
    cnt = 0
    m = 0
    G = []
    h = 1
    while h <= len(A):
        G.append(h)
        h = 3*h+1
    for i in range(m):
        insertionSort(A, n, G[i])

n = int(input())
A = [int(input()) for _ in range(n)]
