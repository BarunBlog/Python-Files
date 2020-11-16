print('Enter three numbers')
a = int(input())
b = int(input())
c = int(input())

# Indentation Error..
# if a>0:
# print('a is a positive number')

if a>0:
    print('a is a positive number')
else:
    print('a is a negative number')

if a%2==0 and b%2==0 and c%2==0:
    print("All numbers are even")
    
elif a%2!=0 or b%2!=0 or c%2!=0:
    print("All numbers are not even")

if b>c:
    print("b is greater than c")
elif c>b:
    print("c is greater than b")
else:
    print("Both are equal\n")
    


name = 'Barun'
if name is 'Barun':
    print('Hello ',name)
    name = name + ' Bhattacharjee'
elif name=='Partho':
    print('Hello ',name)
