# Class & Instance(object) Attributes

class Student:

    college_name="Teerthanker Mahaveer University"  #Class attributes
    name="karan"  #Class attributes

     
    def __init__(self,name,marks):  #Constructor Creation
                                  #Self is Refference of object

        self.name=name   #object attributes > class attributes (precedence)
        self.marks=marks
        print("adding new student in Database..")

s1=Student("nikhil",78)
print(s1.name,s1.marks) 
print(s1.college_name)

s2=Student("Avnish",60)
print(s2.name,s2.marks)
print(Student.college_name)