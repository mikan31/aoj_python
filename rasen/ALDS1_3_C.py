from collections import deque

n = int(input())
linked_list = deque()

for _ in range(n):
    command = input()
    if command[6] == ' ':
        if command[0] == 'i':
            linked_list.appendleft(int(command[7:]))
        else:
            if int(command[7:]) in linked_list: linked_list.remove(int(command[7:]))
    else:
        if command[6] == 'F':
            linked_list.popleft()
        else:
            linked_list.pop()
print(*linked_list)
