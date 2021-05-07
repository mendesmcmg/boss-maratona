n, a, b = map(int, input().split(' '))

pricea = n*a

if pricea < b:
    print(pricea)
else: 
    print(b)