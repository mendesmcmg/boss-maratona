n = int(input())
number = 0

for i in range(1, n+1):
    if (len(str(i))%2)!=0:
        number += 1

print(number)