N = int(input())
A = list(map(int, input().split()))

def SelectionSort(A, N):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if A[minj] > A[j]:
                minj = j
        if minj != i: count += 1
        A[i], A[minj] = A[minj], A[i]
    A_str = [str(i) for i in A]
    print(" ".join(A_str))
    print(count)

SelectionSort(A, N)
