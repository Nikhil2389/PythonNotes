'''
Polymorphism:Operator Overloading

when the same operator is allowed to have different meaning according to the context.

'''
'''
print(1+3)
print(type(1+3)) # 4
print("nikhil"+"kumar")
print(type("Nikhil")) #nikhilkumar
print([1,2,3]+[4,5,6])             
print(type([1,2,3]))  #merge'''

class Complex:
    def __init__(self,real,img):    
        self.real=real                  
  
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __sub__(self,num2):  #we are using dundor function in operator overloading
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1-num2 #this addition is possible using dundor function
num3.showNumber()

'''
Dunder methods are special methods in Python that start and end with
 double underscores (__) and are used to define the behavior of objects.'''
        