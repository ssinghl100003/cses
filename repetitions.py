s = input()
maxcount = 1
currentcount = 1
i = 1
while i < len(s):
    if s[i] == s[i-1]:
        currentcount += 1
        maxcount = max(maxcount, currentcount)
    else:
        currentcount = 1
    i += 1
print(maxcount)