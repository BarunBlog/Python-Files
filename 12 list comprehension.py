li = []
for i in range(1,20):
    li.append(i)

print(li)

## Finding even & odd numbers from li

odd = [item for item in li if item % 2!=0]
print(odd)

## Finding squares

square = []
## [expression for iterator in range(a,b)]

square = [i**2 for i in range(1,10)]
print(square)
