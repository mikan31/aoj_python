N = int(input())
A = list(map(int, input().split()))

def bubbleSort(A, N):
    count = 0
    flag = 1
    while flag == 1:
        flag = 0
        for j in reversed(range(1, N)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1
                flag = 1
    A_str = [str(i) for i in A]
    print(" ".join(A_str))
    return count

count = bubbleSort(A, N)
print(count)
