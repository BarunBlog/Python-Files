import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)

# check if the string has any character between a and n:
x = re.findall("[a-n]", txt)
print(x)

#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)

#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)
