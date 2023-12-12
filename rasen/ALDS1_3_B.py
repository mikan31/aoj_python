from collections import deque

n, q = map(int, input().split())
process = deque([name, int(time)] for name, time in [input().split() for _ in range(n)])

total_time = 0
while True:
    name, time = process.popleft()
    if time > q:
        total_time += q
        process.append([name, time-q])
    else:
        total_time += time
        print(name, total_time)
    if len(process) == 0 : break
