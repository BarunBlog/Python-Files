li = []
for i in range(1,20):
    li.append(i)

print(li)

## Finding even & odd numbers from li

odd = [item for item in li if item % 2!=0]
print(odd)

test1 = [i for i in range(64)]
print(test1)

print("\nprinting 2d list")
test2d = [[0 for col in range(8)] for row in range(8)]
print(test2d)

## Finding squares

square = []
## [expression for iterator in range(a,b)]

print("\npriting square")
square = [i**2 for i in range(1,10)]
print(square)
print()

'''
[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]
if you want to generate all combinations of lists [1,2,3]  and [4,5,6], write:
'''
print([[x,y] for x in [1,2,3] for y in [4,5,6]])
