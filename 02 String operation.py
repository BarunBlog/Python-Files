str1 = "Barun "
str2 = "Hello "+"World"
print(str1+" "+str2)

'''
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
'''

str3 = 'I don\'t think so'
print(str3)

print('Source:D \Barun\Python files\first project.py')
# raw string changed heres
print(r'Source:D \Barun\Python files\first project.py') # r means rush string..
#raw string stays the way you wrote it
str4 = str1+str2
print(str4)

print(str1 * 5)

x = ' '

print(str2.find('World'),x,str2.find('Word'))
print(len(str2))


print(str2.replace('Hello','hello')) # replace returns string but don't replace parmanently
print(str2,"\n")


new_str2 = str2.replace('H','h')
print(new_str2)
print(str2)

str5 = "Hello World!"
print(str5)
del str5
#print(str5) # it will give an error


st1 = "Barun Bhattacharjee"
st2 = "Hello World!"

li = st2.split(" ")
print(li)

st3 = li[0] +' '+ st1
print(st3)

st4 = st2.replace("World!", st1)
print(st4)
