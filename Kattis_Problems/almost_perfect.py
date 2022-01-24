import math

while True:
    try:
        p = int(input())
        dees = []
        for i in range(1, (p-1)):
            if p / i == p // i:
                dees.append(i)
        summ = sum(dees)
        if sum(dees) == p:
            print(p, 'perfect')

        elif abs(summ-p) <= 2:
            print(p, 'almost perfect')
        else:
            print(p, 'not perfect')

    except EOFError:
        break
