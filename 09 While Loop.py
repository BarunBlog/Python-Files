'''
ijfgijfg break
This is a comment
'''

# Two types of loop in python. for & while
print("printing for loop\n")
for i in range(10):
    if i==2:
        i = 6
    print(i, end=" ")
# 0 1 6 3 4 5 6 7 8 9
'''
for i in range(10):
will constantly set i to be the next element in the range 0-10 no matter what you set value of i.
'''
print("\nEquivalent code using while loop will be...")
i = 0
while(i<10):
    if i==2:
        i = 6
    print(i, end=" ")
    i = i + 1

print("\nprinting 1 to 10 using while loop\n")
#printing 1 to 10
i=1
while i<=10:
    print(i)
    i = i+1

#printing fibonacci number
a, b = 0, 1
i=0
N = int(input())
while(i<N):
    a, b = b, a+b
    print(b)
    i+=1
