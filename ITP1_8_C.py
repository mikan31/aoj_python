alph=[0]*26
while True:
    try:
        s=input().lower()
        chara = ord('a')
    except:
        break
    while chara <= ord('z'):
        count = s.count(chr(chara))
        alph[chara-ord('a')] += count
        chara += 1

for i in range(26):
    print("{:s} : {:d}".format(chr(ord('a')+i), alph[i]))
