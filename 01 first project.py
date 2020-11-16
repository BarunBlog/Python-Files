import math
print("Hello World!")

a = 4
b = 6
c = 3.5
Sum = a+b
Sub = a-b
Div = b/c
Mul = a*b
print(Div)
print(Mul)

Div = b//c # floor division
'''
In Python 3,
int/int = float
int//int = int
int//float = intNo.0
'''
print(Div)

Div = math.floor(b/a)
Div1 = math.ceil(b/a)
print('flor & ceil of b/a is ',Div,' ',Div1)

Mul = a**b # b works as power of a
print(Mul)

print(b%a)

myFloat = float(6)
print(myFloat)
print(type(myFloat),' ',id(myFloat))

myFloat = 5
print(myFloat)
print(type(myFloat),' ',id(myFloat))

myFloat = 'Barun'
print(myFloat)
print(type(myFloat),' ',id(myFloat))
