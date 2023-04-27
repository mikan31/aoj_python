input_str = input()
q = int(input())


for _ in range(q):
    command = list(input().split())
    start = int(command[1])
    end = int(command[2])

    if command[0] == 'print':
        print(input_str[start:end+1])
    elif command[0] == 'reverse':
        input_str = input_str[:start] + input_str[start:end+1][::-1] + input_str[end+1:]
    elif command[0] == 'replace':
        input_str = input_str[:start] + command[3] + input_str[end+1:]
    else:
        pass
