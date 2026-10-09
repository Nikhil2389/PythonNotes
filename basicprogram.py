#Sum of two number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum =", sum)

#find odd or even number

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Greatest of two number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

#greatest of three number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#print leap year

year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")