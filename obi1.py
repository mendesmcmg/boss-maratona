n, p = input().split(' ')
n = int(n)
p = int(p)
participants = 0
for i in range(0, n):
    point1, point2 = map(int, input().split(' '))
    if (point1+point2 >= p):
        participants += 1
print(participants)

