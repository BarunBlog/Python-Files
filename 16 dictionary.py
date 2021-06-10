age = {'Barun': 16, 'Rahim': 20, 'Karim': 12, 'Rafi': 26, 'Razu': 20}
print(type(age)," ",age)

print(age['Barun'], ' ' , age['Razu'])

age['Barun'] = 21
print(age)

del age['Rafi']
print(age)

age['Rafi'] = 25
print(age)

for i in age:
    print(i)
print()

print('print all')
for i in age:
    print(i,' ',age[i])
print()

li = age.keys() ## creates a list
for i in li:
    print(i,' ',age[i])
print()

li1 = age.items()
print(age.items(),'\n') ## returns a list of tuples

for i in li1:
    print('yolo ', i)
print()

for key, value in age.items():
    print(key,' ',value)
print()

for x in age.items():
    print(x)
