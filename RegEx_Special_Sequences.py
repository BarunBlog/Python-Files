import re

txt = "The rain in Spain"


#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)

#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)

#Replace all white-space characters with the digit "9":
x = re.sub("\s", "9", txt)
print(x)

#Replace all "Spain" with "Bangladesh":
x = re.sub("Spain", "Bangladesh", txt)
print(x)

txt = "AaBbBg"
# find the sequences of one upper case letter followed by lower case letters, followed bu uppercase ketter
x = re.findall('[A-Z]+[a-z]+[A-Z]', txt)
print(x)
