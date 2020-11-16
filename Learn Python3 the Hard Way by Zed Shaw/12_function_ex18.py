#this one is like scrips with argv
def print_two(*args): #we want to make a function using def for ”define”
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#pointless args
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#no argument
def print_none():
    print("I got nothing")

print_two("Barun","Bhattacharjee")
print_two_again("Barun","Bhattacharjee")
print_one("First!")
print_none()
