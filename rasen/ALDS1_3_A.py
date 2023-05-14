A = list(input().split())
stack = []

for i in A:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    else:
        stack.append(int(i))
print(stack[0])
