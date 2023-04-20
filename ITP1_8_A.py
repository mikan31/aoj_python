s = input()
sd = ''

for i in range(len(s)):
    if s[i].islower(): sd += s[i].upper()
    elif s[i].isupper(): sd += s[i].lower()
    else: sd += s[i]
print((sd))
