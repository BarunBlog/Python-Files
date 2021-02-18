name, age, gender = input().split()

print(name, age, gender)

'''
Problem: take input like following pattern
Take name and list of marks in a line
Input:
    Barun 26.5 45 68 59.4
    Partho 45.9 87.5 78.4 98
'''

name, *line = input().split()
# This input statement will give everythin to the name variable until a space
# and rest of the data will be stored to the line variable as list type.
marks = list(map(float, line))
print(name)

print(marks)
