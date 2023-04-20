while True:
    x = input()
    if x == '0': break
    x_list = list(x)
    x_list = [int(i) for i in x_list]
    print(sum(x_list))
