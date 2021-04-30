n = int(input())
inp = input().split(' ')
listaord = sorted([int(i) for i in inp])
indexa, indexb = ((n//2)-1), (n//2)
resp = listaord[indexb]-listaord[indexa]
print(resp)