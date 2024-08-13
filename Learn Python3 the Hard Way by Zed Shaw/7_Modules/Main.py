import MyModule
#import MyModule as mm
#renaming a module

#import only parts from a module, by using the from keyword.
from AnotherModule import person1

MyModule.myFunction()

str = input("Enter your name: ")
v = int(input("Enter your age: "))
MyModule.myInfo(str,v)


print(person1["age"])
# When importing using the from keyword, do not use the module name when referring
# to elements in the module. Example: person1["age"], not mymodule.person1["age"]
