import re # built-in package can be used to work with Regular Expressions

# Check if the string starts with "The" and ends with "Spain"

txt = "It's raining for 24 hours in Spain all along."
x = re.search("^It.*Spain$", txt)

if x:
    print("Yes! We have a match")
else:
    print("No match")

# Metacharacters
# Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

# Find all digit characters:
x = re.findall("\d", txt)
print(x)

# Search for a sequence that starts with "ra", followed by 4 any characters, and an "g"
x = re.findall("ra....g", txt)
print(x)

# Search for a sequence that starts with "ra", followed by any characters, and an "g"
x = re.findall("ra.*g", txt)
print(x)

#Check if the string contains "ai" followed by 1 or more "n" characters:
x = re.findall("ain+", txt)
print(x)

#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)

#Check if the string contains either "hours" or "stays":
x = re.findall("hours|stays", txt)
print(x)
