while True:
    s = input()
    if s == '-': break
    m = int(input())

    for _ in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)
