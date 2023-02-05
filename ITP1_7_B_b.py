def binary_search(alist, correct):
    minA = 0
    maxA = len(alist)
    count = 0

    while maxA - minA  >=  1:
        mid = (maxA + minA) // 2
        if alist[mid] == correct: return countlist(alist, mid)
        elif alist[mid] < correct: minA = mid + 1
        else: maxA = mid

    return 0

def countlist(alist, match):
    count = 1
    val = alist[match]
    maxint = len(alist) - 1
    i = 1
    while True:
        if match-i < 0: break
        if alist[match-i] == val: count += 1
        else: break
        i += 1
    j = 1
    while True:
        if match+j > maxint: break
        if alist[match+j] == val: count += 1
        else: break
        j += 1
    return count

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0 : break

    alist = []
    count = 0
    for i in range(1, n+1):
        alist = []
        #配列作成
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                alist.append(j+k)

        alist.sort()
        count += binary_search(alist, x-i)
    print(count)
