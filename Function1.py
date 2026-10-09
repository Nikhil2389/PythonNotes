
#Function With One Parameter

'''def greet(name):  #Function Creation
    print("Hello", name)   #Condition

#greet("Nikhil")
greet("aman")  #Function Call
greet("rahul")  #Function Call
greet("shashi")  #Function Call'''

#Add two Number
'''
def add(a, b):  #Function Create
    print(a + b)  #condition

add(10, 20)
add(100,200)   #Function Call'''

#Substract two Number

'''
def subtract(a, b):
    print(a - b)

subtract(20, 5)'''

#Function with Return

'''def add(a, b):
    return a + b

result = add(10, 20)

print(result)'''

#Find Square of Number
'''
def square(n):
    return n * n

num=int(input("enter the number"))
result=square(num)
print(result)'''

#Find Even or Odd

'''def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check(10)
check(7) '''

#Largest of Two Number

'''def largest(a, b):
    if a > b:
        print(a, "is largest") 
    else:
        print(b, "is largest")

largest(20, 10)'''

#Largest of three Number

'''def largest(a, b, c):
    if a > b and a > c:
        print(a, "is largest")
    elif b > a and b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")

largest(10, 30, 20)'''

#Find Factorial of Given Numbetr

'''def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))''' 

#Check Positive Negative or Zero

'''def check(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check(10)
check(-5)
check(0)'''

#Multiplication table

'''def table(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

table(5)'''



#Count Number 1 to N

'''def count(n):
    for i in range(n,0,-1):
        print(i)

count(10)'''

#Sum of Number 1 to N

'''def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

print(sum_numbers(10))'''


#Fuction with List

'''def show_list(items):
    print("List:", items)

fruits = ["Apple", "Banana", "Mango"]

show_list(fruits)'''

#Function with Tupple

'''def show_tuple(data):
    print("Tuple:", data)

numbers = (10, 20, 30)

show_tuple(numbers)'''


#Function with Strings

'''def greet(name):
    print("Hello", name)

student = "Nikhil"

greet(student)'''

#Reverse a String 
'''
def reverse_string(text):
    rev = ""

    for ch in text:
        rev = ch + rev

    return rev

#word = "Python"

word=str(input("enter the string"))

print(reverse_string(word))'''

'''
def Name(name):
    print("your name is:",name)

Name("nikhil") '''

'''
def SumNumber(n):
    sumOdd=0
    for i in range(1,n+1,2):
        sumOdd=sumOdd+i

    return sumOdd
num=int(input("enter the number"))

result=SumNumber(num)
print(result)'''

'''
def Name(name):
    print("you name is",name)

Name("nikhil") 
Name("aman") '''

'''
def oddEven(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

oddEven(6)'''

def sumNumber():
    number=[2,4,5,6,3,7,9] 
    sumOdd=0

    for i in number:
        if i % 2 !=0:
          sumOdd=sumOdd+i

    return sumOdd


result=sumNumber()
print(result)   


