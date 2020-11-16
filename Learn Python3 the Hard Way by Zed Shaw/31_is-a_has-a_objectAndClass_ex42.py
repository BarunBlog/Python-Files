## Animal is-a object
class Animal(object):
    def __init__(self, animalName, petName):
        ## Animal has-a __init__ that takes self, animalName & petName params
        self.animalName = animalName
        self.petName = petName

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a __init__ that takes self & name params
        super(Dog, self).__init__("Dog",name)
        self.name = name


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a __init__ that takes self & name params
        super(Cat, self).__init__("Cat",name)
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a __init__ that takes self & name params
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a __init__

        super(Employee, self).__init__(name)
        ##Employee has-a salary attribute
        self.salary = salary

## Fish is-a object
class Fish(object):
    def __init__(self, fishType, name):
        ## Fish has-a __init__ that takes self, fishType & name params
        self.fishType = fishType
        self.name = name

## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, name):
        ## Salmon has-a __init__ that takes self & name params
        super(Salmon, self).__init__("Salmon",name)
        self.name = name

## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self, name):
        ## Salmon has-a __init__ that takes self & name params
        super(Halibut, self).__init__("Halibut",name)
        self.name = name


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is a Fish
flipper = Fish("","")

## crouse is-a Salmon
crouse = Salmon("Mary")

## harry is-a Halibut
harry = Halibut("Bel")
