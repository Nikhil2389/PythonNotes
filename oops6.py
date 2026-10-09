class Student:

    def __init__(self,name):
        self.name=name #public

s1=Student("nikhil")
#print(s1)
print(s1.name)
del s1.name
print(s1.name)