# Static Methods

'''
Methods that do not use the self parameter (work at class level)

Note:- Decorators allow us to wrap another function in order to extend the behavior
of the wrapped function,without permanently modifying it.

'''

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod     #Decorators
    def hello():
        print("hello")    

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print("hi",self.name,"your age is:",sum/3)        


s1=Student("nikhil",[78,89,60])
s1.get_avg()

s1.name="akash" #Changing the name
s1.get_avg()
s1.hello()

'''
class student:
    school="giat"


    @classmethod
    def show_school(cls):
        print(cls.school)

student.show_school() '''       
        

