print('Enter the elements of list: ',end=" ")

li=[]
li = list(map(int,input().split()))

for i in li:
    for j in li:
        if i==j:
            continue
        
