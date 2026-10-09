# Methods
'''
Methods are function that belong to object.

class:

1.data(attributes)
2.methods

'''

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def welcome(self):
       
       print("welcome student:",self.name)

    def get_marks(self):
       print("your marks is :",self.marks)
       #return self.marks            



s1=Student("nikhil",78)
s1.welcome()
s1.get_marks()
#print(s1.get_marks())

    