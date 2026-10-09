#String Declaration,String Initialization,String Accessing.
# string is a sequence of character
'''name = "Nikhil"

print(name)  #string printing
print(name[0])  #string Access
print(name[1])
print(name[2])
print(name[-1])
print(name[-2])'''



#Taking input from String.
'''name=str(input("eneter the name:"))
print("your name is:",name)'''


#Print the String Character in the next line.

'''name = "Nikhil"

for ch in name:
    print(ch)'''
#Find the vowels in the String.
'''
text = str(input("Enter a string: "))

for ch in text:
    if ch.lower() in "aeiou":
        print(ch) '''

#Change the String lower to upper.

'''text = input("Enter a string: ")

print(text.upper())'''

#Reverse a String.

'''text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)'''

#Find the Consonants in the String.

'''text = input("Enter a string: ")

for ch in text:
    if ch.lower() in "bcdfghjklmnpqrstvwxyz":
        print(ch)'''


#Copy a given String.
'''
text1 = input("Enter a string: ")

text2 = text1

print("Original:", text1)
print("Copied:", text2) '''

#Print each character of a string using a for loop.
'''text = input("Enter a string: ")

for ch in text:
    print(ch)'''

#find the length of a string without using len().

'''text = input("Enter a string: ")

count = 0

for ch in text:
    count += 1

print("Length =", count)'''

#Check wether a string is a palindrome or not.

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count the frequency of each characters.

'''text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)'''


#Find the first non repeating character.
'''
text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break '''

#Write a Function that returns the characters with the highest frequency.

'''def highest_frequency(text):

    frequency = {}

    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    highest_char = ""
    highest_count = 0

    for ch in frequency:
        if frequency[ch] > highest_count:
            highest_count = frequency[ch]
            highest_char = ch

    return highest_char


text = input("Enter a string: ")

result = highest_frequency(text)

print("Highest frequency character:", result)'''