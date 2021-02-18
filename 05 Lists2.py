li = ["computer", "mobile", "cell phone", "laptop"]
print(li[1]," ",li[3], "\n")
li3 = li[:]

print(li,' ',len(li), "\n")

print(li[-1],' ',li[-2], "\n")

li2 = ["computer", 10, 12.5, "Banglades"]
print(type(li2[2]), "\n")

print(li[-2:], "\n")
print(li[:-1], "\n")

print(li[0:4:1], "\n")
print(li[0:4:2], "\n")
print(li[0:4:3], "\n")

print(li[::1], "\n")
print(li[::-1], "\n") #List reversed

li[2] = "mobile phone"

li = li+['pencil']

li.append("mouse")
print(li, "\n")

# inserting elements to the given index
li.insert(1, "keyboard")
print(li, "\n")

li.remove('pencil')
print(li, "\n")

del li[4]
print(li, "\n")

del li[1:3]

print(li2,"\n")
remove = li2.pop()
print(li2, "\n")

li2.pop(1)
print(li2,"\n")


#Sort
li3.sort()
print(li3)

li3.clear()
