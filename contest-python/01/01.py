a, b = map(int, input().split(' '))

if a >= 13:
    cost = b
    print(cost)
    #print(f'Takahashi is {a} years old, and the cost of the Ferris wheel is {cost} yen.')
elif a < 13 and a > 5: 
    cost = int(b/2)
    print(cost)
    #print(f'Takahashi is {a} years old, and the cost of the Ferris wheel is the half of {b} yen, that is, {cost} yen.')
else: 
    cost = 0
    print(cost)
    #print(f'Takahashi is {a} years old, and he can ride the Ferris wheel for free.')