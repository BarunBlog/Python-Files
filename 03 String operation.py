## These operation doesn't change the string

str1 = ' Barun '
print(str1,' ',len(str1))

# The strip() method removes any whitespace from the beginning or the end
str2 = str1.strip()
print(str2,' ',len(str2))
print(str1,' ',len(str1))

# Remove spaces to the left of the string
str3 = str1.lstrip()
print(str3,' ',len(str3))

# Remove spaces to the Right of the string
str4 = str1.rstrip()
print(str4,' ',len(str4))

str5 = 'AbcDFi'
print(str5.upper())

print(str5.lower())


# String swap
str6 = 'Bangla'
str7 = 'desh'
str6, str7 = str7, str6
print(str6,' ',str7)

# Character access
print(str5[0])
print(str5[-1],' ',str5[-2])

print(str5[1:4])
print(str5[:5])
print(str5[1:])
print(str5[:])

## print ascii value of char
st = 'Barun'
ln = len(st)
for i in range(0,ln-1):
    a = ord(st[i])
    print(a, end=" ")

print(ord(st[ln-1]))
