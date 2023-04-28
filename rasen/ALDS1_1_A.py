N = int(input())
A = list(map(int, input().split()))
A_str = [str(i) for i in A]
print(" ".join(A_str))

def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        A_str = [str(i) for i in A]
        print(" ".join(A_str))

insertionSort(A, N)
