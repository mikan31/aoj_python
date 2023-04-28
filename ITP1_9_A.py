W = input()
W_num=0

while True:
    T = input()
    if T == 'END_OF_TEXT': break
    sentence = T.lower().split()
    W_num+=sentence.count(W)

print(W_num)
