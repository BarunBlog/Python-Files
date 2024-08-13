myLists1 = [10,12,16,20,29]
print(myLists1)
print(myLists1[2],' ',myLists1[-1])

myLists1[2]=18
print(myLists1)

myLists2 = myLists1+[35,40,43]
print(myLists2)


myLists1.append(30)
print(myLists1)

print(myLists1[:2])
myLists1[1:3]=[1,2]
print(myLists1)


myLists1[:2]=[] ## delets values of list to index 2(excluding)
print(myLists1)

myLists1[:]=[] ## delets entire list
print(len(myLists1))



