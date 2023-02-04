while True:
    a,op,b = input().split()
    if op == '?': break
    if op == '/':
        print(eval(a + '//' + b))
    else:
        print(eval(a + op + b))
