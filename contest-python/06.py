n, x = map(int, input().split(' '))
coords = list(map(int, input().split(' ')))
bounces = [0]
allowed = 0

for i in range(0, n):
    bounces.append(bounces[i]+coords[i])
    if bounces[i]<=x:
        allowed += 1
print(allowed)
print(bounces)