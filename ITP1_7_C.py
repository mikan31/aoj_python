r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]
sum_line = 0
sum_line_list = []

# 横について
for i in range(0,r):
    sum_line = 0
    for j in range(0, c):
        print("{:d} ".format(table[i][j]), end="")
        sum_line += table[i][j]
    print(sum_line)
    #output.append(table[i] + [sum_line])

# 縦について
for i in range(0,c):
    sum_line = 0
    for j in range(0, r):
        sum_line += table[j][i]
    sum_line_list.append(sum_line)
print(" ".join(map(str, sum_line_list)), end="")
print(" {:d}".format(sum(map(int, sum_line_list))))
