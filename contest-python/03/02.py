a, b, c = map(int, input().split(' '))
cap = a - b
transf = c - cap
if transf < 0:
    print(0)
else:
    print(transf)