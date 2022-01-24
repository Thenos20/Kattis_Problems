t = int(input())
n = int(input())
a = {}

# dad: middle-middle-middle-lower-middle class
# mom: upper-upper-lower-middle class
for e in range(t):
    a = {}
    for i in range(n):
        nn = 0
        score = 1
        b = input().split()
        a.__setitem__(b[0], b[1])
        x = a[b[0]]

        #print(a)
        x = x.split('-')
        copyx = x.copy()
        a[b[0]] = 0
        for o in range(10-len(x)):
            copyx.insert(0, 'middle')
        for q in range(10):
            if 'upper' in copyx[nn]:
                score = 3
            elif 'middle' in copyx[nn]:
                score = 2
            else:
                score = 1
            a[b[0]] += score*10**nn
            nn += 1
        #print(x)
        #print(copyx)
        #print(a[b[0]])
    a = {k: v for k, v in sorted(a.items())}
    a = dict(reversed(list(a.items())))
    #print(a)
    a = sorted(a.items(), key=lambda x: x[1])
    #print(a)
    sortdict = dict(a)
    #print(sortdict)
    res = dict(reversed(list(sortdict.items())))
    #print(res)
    for key in res.keys():
        print(key.replace(':', ''))
    print('='*30)