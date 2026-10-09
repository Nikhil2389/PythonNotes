'''class Method:A class method is bound to the class
  & receives the class as in implicit first argument
  
  Note:static method cant access or modify class state & generally for utility'''

class Person:
    name="aman"

    #def changeName(obj,name):
    #self.__class__.name="rahul"

    @classmethod
    def changeName(cls,name):
        cls.name=name


p1=Person()
p1.changeName("nikhill kumar")
print(p1.name)
print(Person.name)        