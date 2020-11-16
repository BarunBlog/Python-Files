stuff = {'name':'Barun', 'age':22, 'height':5*12+10}
print(stuff['name'])

print(stuff['age'])

print(stuff['height'])

stuff['city'] = "Sylhet"

print(stuff['city'])
stuff['city'] = "Dhaka"

stuff[2] = 'Partho'
stuff[3] = 'Wow'

print(stuff[2])
print(stuff[3])

print(stuff)

del stuff['city']
del stuff[2]
del stuff[3]
print(stuff)
