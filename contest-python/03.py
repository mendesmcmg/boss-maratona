a, b = map(int, input().split(' '))
pies = 0
pieces = (a*3)+b

if pieces >= 2:
    pies = int(pieces/2)

print(pies)
