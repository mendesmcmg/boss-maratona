a, b = map(int, input().split(' '))

roadarea = a+b-1
yardarea = (a*b)-roadarea
print(yardarea)