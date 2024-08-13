
class Person:
    #class Person(object): #python 2 # Generally, object is made ancestor of all classes

    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# definition of subclass starts here
class Student(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        Person.__init__(self, student_name, student_age)
        #super(Person,self).__init__(student_name, student_age) #in python 2
        #super().__init__(student_name, student_age) #in python 3
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


# end of subclass definition


# Create an object of the superclass
person1 = Person("Richard", 23)
# call member methods of the objects
person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.get_id())
student1.show_name()

#https://github.com/wzpan/Learn-Python-The-Hard-Way/
#https://github.com/BarunBlog?tab=repositories
#https://guides.github.com/activities/hello-world/
#https://github.com/hasancse91/Programming-Problem-In-Bengali
