
# def recursiva(n, sides, lista2, lista3, restantes):
#   ways = 0
#   if ways == 3*n:
#     return ways
  

# def main():
#   n = int(input())
#   sides = list(map(int, input().split(' ')))
#   olhando = 0
#   lista2=[]
#   lista3=[]
#   restantes=sides.copy()
#   print(recursiva(n, sides, lista2, lista3, restantes))

###2
# n = int(input())
# sides = list(map(int, input().split(' ')))
# ways = 0
  
# for i in range(0, n):
#   for j in range(0, n):
#     for k in range(0, n):
#       if sides[i]!=sides[j] and sides[j]!=sides[k] and sides[i]!=sides[k] and i!=j and i!=k and k!=j:
#         if sides[i]>abs(sides[j]-sides[k]) and sides[i] < sides[j]+sides[k]:
#           ways+=1
# print(ways)

