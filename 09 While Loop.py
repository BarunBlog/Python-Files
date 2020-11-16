'''
ijfgijfg break
This is a comment
'''

# Two types of loop in python. for & while

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

