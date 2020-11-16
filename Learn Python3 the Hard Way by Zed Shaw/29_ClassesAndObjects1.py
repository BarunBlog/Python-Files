#python 3 class definition
'''
class MyClass:
    pass
'''


class Employee:

    empCount = 0
    #The first method __init__() is a special method, which is called
    #class constructor or initialization method that Python calls when
    #you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    #You declare other class methods like normal functions with the
    #exception that the first argument to each method is self. Python
    #adds the self argument to the list for you; you do not need to
    #include it when you call the methods.

    def displayCount(self):
        print(f"Total Employee {Employee.empCount}")

    def displayEmployee(self):
        print("Name : ",self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()
print(f"Total Employee {Employee.empCount}\n")
