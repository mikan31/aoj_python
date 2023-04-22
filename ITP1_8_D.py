import sys

s = input()
p = input()

for index in range(len(s)):
    exist=True
    for i in range(len(p)):
        if s[(index+i)%len(s)] != p[i]:
            exist=False
            break
    if exist == True:
        print('Yes')
        sys.exit()
print('No')
