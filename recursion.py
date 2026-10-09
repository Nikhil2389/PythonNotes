'''
Recursion :- Recursion is a technique where a function calls itself to solve a problem.


A recursive function must have 2 parts:

  1.Base Case → Stops the recursion.

  2.Recursive Case → Calls the function again with a smaller problem.

  '''

#Print 1 to N
'''
def print_num(n):                   
    if n == 0:   # Base case
        return

    print_num(n-1) # Recursive case
    print(n)

print_num(5)  #function calling '''
'''
def number(n):
    if n==0:
        return
    
    number(n-1)
    print(n)
num1=int(input("enter the number"))
number(num1)  '''  

#Print N to 1
'''
def reverse_num(n):
    if n == 0:   #Base Case
        return

    print(n)
    reverse_num(n-1) #Recursive Case
     

reverse_num(5) '''

#Factorial of given number
'''
def factorial(n):
    if n == 1:  #base case          
        return 1

    return n * factorial(n-1)  #recursive case

print(factorial(5))'''

#Sum of Number

'''def total(n):
    if n == 1:
        return 1

    return n + total(n-1)

print(total(5))'''

#Fibonacci Series

'''def fib(n):
    if n == 0 or n == 1: #base case
        return n

    return fib(n-1) + fib(n-2) #recursive case

for i in range(7):
    print(fib(i), end=" ")'''

#Reverse a String using Recursion

'''def reverse(text):
    if text == "":
        return ""

    return reverse(text[1:]) + text[0]

print(reverse("Python"))'''

#Check Even or Odd 
'''
def even_odd(n):
    if n == 0:
        return "Even"
    if n == 1:
        return "Odd"

    return even_odd(n - 2)

print(even_odd(8))
print(even_odd(7))'''

def square(n):
    if n:
        return n


    return n * square(n)


     

print(square(5))



#check number is prime or not

'''def is_prime(n, i=2):
    if n <= 1:
        return False

    if i == n:
        return True

    if n % i == 0:
        return False

    return is_prime(n, i + 1)

num = 13

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")'''

#Largest of two numbers

'''def largest(a, b):
    if a > b:
        return a
    return b

print(largest(10, 25))'''

#Largest of three numbers

'''def largest_two(a, b):
    if a > b:
        return a
    return b

def largest_three(a, b, c):
    return largest_two(a, largest_two(b, c))

print(largest_three(18, 45, 30))'''

