from itertools import product

n = int(input())
elements = []

for i in range(0,n):
    li = list(map(int, input().split()))
    elements.append(li)

print( list(product(*elements)) )
