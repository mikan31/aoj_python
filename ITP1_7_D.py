n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[0]*l for _ in range(n)] #出力する配列の定義

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
        if j == 0 : print(C[i][j], end="")
        else: print(" {:d}".format(C[i][j]), end="")
    print()
