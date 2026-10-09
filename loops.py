# Loops in Python
'''
loops are used to execute a block of code repeatedly until a condition is met
or items in a sequence are processed

Types of Loops in Python

1.For Loop
2.While Loop 
3.Infinite while loop 
4.Nested Loop '''



'''n = 4
for i in range(0, n,2):
 print(i) '''

# Counting Positive Number

'''numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count=0

for num in numbers:
    if num>0:
        positive_number_count = positive_number_count + 1
print("final count of positive number is:", positive_number_count)'''


# Sum of Even Numbers
'''
n=[1,2,3,4,5,6,7,8,9,10]         
sum=0

for i in n:
    
    sum=sum+i
print("sum of even number is:",sum) '''

#Sum of odd Number

'''
sum_odd=0

for i in range(1, 11):                  
    if i%2!=0: 
        sum_odd=sum_odd+i
print("sum of odd number is:",sum_odd)'''

    
#sum of Number
'''
sum = 0

for i in range(1,6):
    sum = sum + i   

print(sum)'''

#Print Multiplication table 

'''for i in range(5,51,5):
    print(i)'''

'''n=5 
for i in range(1,11):
    if i==5:
        continue
    print(n,"*",i,"=",n*i)'''

#Reverse a String
'''
input_str="python"
reversed_str=""

for char in input_str:               
    reversed_str=char+reversed_str     

print(reversed_str)'''


#Non Reapeted Number
'''
input_str="aabccddfee"

for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print("char is:",char)
        break '''

# Calculate the factorial of given number
'''number=5
factorial=1'''

'''while number>0:
    factorial=factorial*number
    number=number-1
print("factorial:",factorial)'''

#check number is valid or not

'''while True:
    number=int(input("enter the number b/w 1 and 10: "))
    if 1<=number<=10:
        print("thanks")
        break
    else:
        print("invalid number,try again")'''

#check number is prime or not
'''
number=46

is_prime=True

if number>1:
    for i in range(2,number):
        if(number%i)==0:
            is_prime=False
            break
print(is_prime) '''




#while loop
'''
n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("sum =", sum)  '''

#for loop
'''
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


fact=1

for i in range(1,6):
    fact=fact*i

print(fact)'''

        
name=str(input("enter your name: "))

count=0
for ch in name:
    if ch in "aeiouAEIOU":
        count=count+1
print("Total count of vowel:",count)







