my_name = 'Barun Bhattacharjee'
my_age = 22 #not a lie
my_height = 69 #inches
my_weight = 125 #lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.") # strings have variables embedded in them
print(f"He's {my_height} inches tall.")# start the string with the letter f for ”format”
print(f"He's {my_weight} pounds heavy.")# as in f"Hello {somevar}"
print(f"Actually that's not too skinny.") #This little f before the " (double-quote) and the {} characters tell Python
                                           #3, ”Hey, this string needs to be formatted. Put these variables in there.”
print(f"He's got {my_eyes} eyes and {my_hair}hair.")
print(f"His teeth are usuall {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
