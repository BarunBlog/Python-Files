#python 2.x class definition
'''
class MyClass(object):
    pass
'''


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I Am Classy apples!")

thing = MyStuff() # object created
thing.apple()
print(thing.tangerine)
