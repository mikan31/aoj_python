r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]
output = []
sum = 0
sum_list = []

# 横について
for i in range(0,r):
    sum = 0
    for j in range(0, c):
        print("{:d} ".format(table[i][j]))
        sum += table[i][j]
    print(sum)
    #output.append(table[i] + [sum])

# 縦について
for i in range(0,c+1):
    sum = 0
    for j in range(0, r):
        sum += output[j][i]
    sum_list.append(sum)
print(" ".join(map(str, sum_list)))
#output.append(sum_list)
