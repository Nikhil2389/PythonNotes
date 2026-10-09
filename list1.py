# sum of list
'''
num=[2,4,3,5,6,7]
sum=0

for i in num:
    sum=sum+i
print("sum of number is:",sum)'''



#largest number in list

num=[3,4,5,6,1,8,9]
largest=num[0]

for i in num:
    if i>largest:
     largest=i
print("largest number is =",largest)



#smallest number in list
'''
num=[2,3,5,8,0,1,3,9]
smallest=num[0]

for i in num:
   if i<smallest:
      smallest=i
print("smallest number is=",smallest) '''


#Reverse a list without using reverse method

num=[3,2,5,7,0,8]

for i in range(len(num)-1,-1,-1):
     print(num[i],end=" ")

#Average of number in list
'''
num=[3,1,4,5,8,9,0]
sum=0

for i in num:
    sum=sum+i

avg=sum/len(num)

print("Average=",avg)'''


#Find the given element is found in the list or not

num=[3,4,2,5,7,9,0,6]
key=8
found=False


for i in num:
    if i==key:
        found=True
if found==True:
    print("found")

else:
    print("not found")  

#Find total even number in the list
'''
num=[3,5,2,6,8,9]
count=0

for i in num:
    if i%2==0:
        count=count+1

print("count of even number is:",count)'''


#find the count of postive number and also negative number
'''
num=[2,6,4,-4,-2,5,-1]
postive=0
negative=0

for i in num:
    if i>0:
        postive=postive+1
    elif i<0:
        negative=negative+1

print("count of positive number:",postive)
print("count of negative number:",negative)        
    
'''

