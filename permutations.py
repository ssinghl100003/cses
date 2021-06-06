n = int(input())
if n == 1 or n > 3:
    res = []
    for i in range(2, n+1, 2):
        res.append(i)
    
    for i in range(1, n+1, 2):
        res.append(i)
    
    print(*res)
else:
    print('NO SOLUTION')