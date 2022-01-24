import math

m, n, t = input().split()
n = int(n)
m = int(m)
t = int(t)
tdic = {
    1: (math.factorial(n)),
    2: 2**n,
    3: n**4,
    4: n**3,
    5: n**2,
    6: n*math.log2(n),
    7: n
}

if m < tdic[t]:
    print('TLE')
elif m >= tdic[t]:
    print('AC')
