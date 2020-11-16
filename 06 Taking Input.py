inp = input('Take an int value: ')
print(inp)  # returns a string value
print(type(inp))
inp = int(inp) # converting to integer 
print(type(inp))

#Taking 3 input sparated by spaces
print("Take 3 input sparated by spaces")
a,b,c = input().split(" ")
print(a," ",b," ",c)

#Taking 3 input sparated by comma
print("Take 3 input sparated by comma")
a,b,c = input().split(",")
print(a," ",b," ",c)

name = input('What is your name? ')
print('Hello ',name)

##SUM
num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')
num1 = int(num1)
num2 = int(num2)
addition = num1+num2
print("Sum of two numbers are: ",addition)

##Division
num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
div = num1 / num2
print(div)


nmbr = input('Enter a number: ')
nmbr = int(nmbr)
sqr = nmbr*nmbr
print('Square of number ',nmbr,' is',sqr)





