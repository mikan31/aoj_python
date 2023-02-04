while True:
    a, op, b = input().split()
    a, b = int(a), int(b)

    if op == '?':
        break
    elif op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        # 小数点以下を切り捨て
        print(a//b)
