while True:
    x, y = map(int, input().split())
    if (x == 0) & (y == 0): break
    if x <= y :
        print(x,y)
    if x > y :
        print(y,x)
