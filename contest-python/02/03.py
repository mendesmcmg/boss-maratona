a, b = map(int, input().split(' '))
comp = a
resp = []
if b > a:
    comp = b

for i in range(0, comp):
    if abs((a - i)) == abs((b - i)):
        resp.append(i)

if resp == []:
    print('IMPOSSIBLE')
else:
    stringResp = ' '.join([str(item) for item in resp ])
    print(stringResp)

##TLE