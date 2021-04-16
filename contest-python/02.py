r, d, x = map(int, input().split(' '))
total = 0
ant = 0

for i in range(0, 10):
    if i == 0:
        total += (r*x)-d
        ant = total
    else:
        total = (ant*r)-d
        ant = total
    print(total)