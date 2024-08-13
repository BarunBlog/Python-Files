## These operations change the list permanently

li = [1,6,7,2,10,3,5,7,4]
print(li)

li.reverse()
print(li)

li.sort()
print(li)

li.append(8)
print(li)
#[1, 2, 3, 4, 5, 6, 7, 7, 10, 8]

li.insert(1,5) ## 5 is inserted at postion 1.
print(li)
#[1, 5, 2, 3, 4, 5, 6, 7, 7, 10, 8]

li2 = [10,11,23,15,20]
li.extend(li2) ## 2 lists are extended
print("li after extend ", li)

li3 = [1,2,2,3,5,6,6]
li3.remove(2)
print(li3)

li3.pop()
print(li3)

li3.pop(1) # number poped at position 1
print(li3)

#Initialize list by 0 with size 100
li4 = [0]*100
print(li4)

#Copy of lists. Here also adress of li3 is copied to li5
li5 = li3
print(li5)

li3.append(8) #Both lists will be changed
print(li3)
print(li5)
