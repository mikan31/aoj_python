W, H, x, y, r = map(int, input().split())

flag = 0
if (r <= x) & (x <= W - r):
    if (r <= y) & (y <= H - r):
        flag = 1

if (flag == 1):
    print('Yes')
else:
    print('No')
