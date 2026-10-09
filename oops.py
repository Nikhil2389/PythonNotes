# OOP in python

'''To map with real world scenarios,we started using objects in code.
this is called object oriented progamming.'''

#Procedural Programming

'''a=10
b=20
sum=a+b
print(sum)
diff=a-b
print(diff)'''


#Functional Programming

'''def sum(a,b):
    print(a+b)

sum(10,20)
sum(30,60)'''


'''def sum(a,b):
    return a+b

result=sum(10,40)
print(result)'''



'''def add(a,b):
    return a+b
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

result=add(num1,num2)
print("sum=",result)'''

#Object Oriented Programming

#Class and Object in Python

#class is a blueprint for creating object

class Student:  #Creating Class
    name="nikhil"
    marks=67

s1=Student()   #Creating Object(instances of class)
print(s1.name)
print(s1.marks)


class Car:   #Creating Class 
    color="blue"
    brand="mercedes"

car1=Car()   #Creating Object
print(Car.color)
print(Car.brand) 


#__init__ Function(Constructor)

'''
all classes have a function called _init_(),
which is always executed  when the object is being initiated.
'''

class Student:


    def __init__(self,name,marks,age):  #Constructor Creation
                                  #Self is Refference of object

        self.name=name
        self.marks=marks
        self.age=age
        print("adding new student in Database..")

s1=Student("nikhil",78,22)
print(s1.name,s1.marks,s1.age) 

s2=Student("Avnish",60,25)
print(s2.name,s2.marks,s2.age)


#There are two types of Constructor

# 1. Default Constructor
'''
def __init__(self):
    pass

# 2. Parameterized Constructor

def __init__(self,name,marks):  #Constructor Creation
                                  #Self is Refference of object

        self.name=name
        self.marks=marks
        print("adding new student in Database..")'''



'''
Note:-
the self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.

'''


'''
class student:
     name="nikhil"
     age=34
     marks=89


s1=student()
print(s1.name) 
print(s1.age)
print(s1.marks) '''   





     






   


    


