bl = True
print(bl,' ',type(bl))

ml = bool(False)
print(ml)

ml = bool(0)
print(ml)

ml = bool(2)
print(ml," ", bool(100)," ",bool(10*0))

print(bool(' '), " ", bool('string'), " ", bool(''))

print(bool([1,2,3]), " ", bool([1]), " ", bool([]), "\n")

bl = True
bl = not bl
print(bl)

bl = not bl
print(bl)

a = False
b = True
print(a and b)
print(a or b,"\n")

#Searching a number in list
li = [1,2,3,4]
print(3 in li)
print(6 in li)

li1 = ['Barun','Bhattacharjee','Partho']
print('Barun' in li1)
