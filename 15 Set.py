a = set()
print(type(a))

## Set function only takes an iterable object as an argument. Example: list, tuple..
tpl = (1,2,3,4,5)
a = set(tpl)
print(type(a)," ",a)

li = [2,3,5,8]
b = set(li)
print(type(b)," ",b)

## Union operation
print(a | b)

## Intersection operation
print(a & b)

## Uncommon in both
print(a ^ b)

## Finding a number in set
print(7 in a," ",8 in b)

c = set('abdcd')
print(c) #don't sort string

# Set only takes distinct numbers
li1 = [1,1,2,3,5,2,3,9,8,5]
d = set(li1)
print(d)

li1 = list(d) #Set to List
print(li1)
