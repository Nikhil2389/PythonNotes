'''
Q.1 Create student class that takes name & marks of 3 subject as argument in constructor.
 Then create a method to print the average

'''

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print("hi",self.name,"your marks is:",sum/3)        


s1=Student("nikhil",[78,89,60])
s1.get_avg()

s1.name="akash" #Changing the name
s1.get_avg()
        