n = int(input())

table = [[False for _ in range(13)] for _ in range(4)]
mark_chara = ['S', 'H', 'C', 'D']


def get_index(mark_str):
    for i in range(4):
        if mark_str == mark_chara[i]:
            return i
    return -1

for _ in range(n):
    li = list(map(str, input().split()))
    mark = get_index(li[0])
    num = int(li[1]) - 1
    table[mark][num] = True

for mark in range(4):
    for num in range(13):
        if table[mark][num] == False:
            print("{:s} {:d}".format(mark_chara[mark], num + 1))
