str1 = input('Take 1st string input: ')

if str1.islower() == True:
    print('String’s alphabetic characters are all lower case')
    
elif str1.isupper() == True:
    print('String’s alphabetic characters are all upper case')
else:
    print(':(  :(')

str2 = input('Take 2nd string input: ')
str2 = " ".join(str2)
print(str2) ## method to add whitespace to that string



str2 ="Hello Barun Bhattacharjee"

print(str2.split()) ## split function returns list of strings 
print(str2.split(" ")[0])

print(str2.split("Hello"))



str3 = 'Barun Bhattacharjee'
print(str3.replace('Barun','Partho'))
