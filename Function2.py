'''
Function Method
  
  
1. Call by Value (Immutable Objects)

In Python, numbers, strings, and tuples are immutable. When you pass them to a function,
changing the parameter does not change the original variable.


2.Call By Refference(Mutable Objects)

Python does not have true call-by-reference like C++. But lists and dictionaries are mutable,
so changes inside the function affect the original object.

'''
'''
# 1.Call by Value


def change(x):
    x = 100
    print("Inside:", x)

a = 10
change(a)

print("Outside:", a)'''
'''
# 2.Call by Refference
def add_item(lst):
    lst.append(40)

numbers = [10, 20, 30]
  

add_item(numbers)

print(numbers)'''

#Call by Value

def swap(a, b):
    temp = a
    a = b
    b = temp

    print("Inside function:", a, b)

x = 10
y = 20

swap(x, y)

print("Outside function:", x, y)


#Call by Refference

def swap(nums):
    temp = nums[0]
    nums[0] = nums[1]
    nums[1] = temp

    print("Inside function:", nums)

numbers = [10, 20]

swap(numbers)

print("Outside function:", numbers)




