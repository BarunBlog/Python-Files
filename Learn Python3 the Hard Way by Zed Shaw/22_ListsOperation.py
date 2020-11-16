li = [1,6,7,2,10,3,5,7,4]
print(li)
#[1,6,7,2,10,3,5,7,4]

li.reverse()
print(li)
#[4,7,5,3,10,2,7,6,1]

li.sort()
print(li)
#[1,2,3,4,5,6,7,7,10]

li.append(8)
print(li)
#[1,2,3,4,5,6,7,7,10,8]

li.insert(1,5) # 5 in inserted at position 1.
print(li)
#[1,5,2,3,4,5,6,7,7,10,8]

li2 = [10,11,23,15,20]
li.extend(li2)
print(li)
#[1, 5, 2, 3, 4, 5, 6, 7, 7, 10, 8, 10, 11, 23, 15, 20]

li3 = [1,2,2,3,5,6,6]
li3.remove(2) #number at position 2 is removed
print(li3)
#[1,2,3,5,6,6]

li3.pop()
print(li3) #last element will be deleted
#[1,2,3,5,6]

li3.pop(1)#number poped at position 1
print(li3)
#[1,3,5,6]

li4 = [0]*100 #Initialize list by 0 with size 100
print(li4)

#Copy of lists. Here also adress of li3 is copied to li5
li5 = li3
print(li5)

li3.append(8)#Both lists will be changed
print(li3)
print(li5)
