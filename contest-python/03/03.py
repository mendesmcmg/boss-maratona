a, b = map(int, input().split(' '))

values = [a+b, a-b, a*b]
val = sorted(values)
print(val[2])
