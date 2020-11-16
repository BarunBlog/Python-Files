li = ["computer", "mobile", "cell phone", "laptop"]
print(li[1]," ",li[3], "\n")
li3 = li[:]

print(li,' ',len(li), "\n")

print(li[-1],' ',li[-2])

li2 = ["computer", 10, 12.5, "Banglades"]
print(type(li2[2]))

print(li[-2:])
print(li[:-1])

print(li[0:4:1])
print(li[0:4:2])
print(li[0:4:3])

print(li[::1])
print(li[::-1]) #List reversed

li[2] = "mobile phone"

li = li+['pencil']

li.append("mouse")
print(li)

li.remove('pencil')
print(li)

del li[4]
print(li)

del li[1:3]

remove = li2.pop()
print(li2)

li2.pop(2)
print(li2,"\n")


#Sort
li3.sort()
print(li3)

li3.clear()
