a, b = map(int, input().split(' '))
res = 0

if a%b == 0:
    print(int(a/b))
else:
    if a > b:
        res = b+(a-b)
    elif b > a:
        res = (b-a)+a
    print(res)