# all list method in python

a = [10, 20]

# 1.append() :add the items from end

'''
a.append(30)
print(a) ''' 

# 2.extend() :add the multiple items
'''
a.extend([40, 50])
print(a)'''

# 3.insert() :add the itms on any index

a.insert(1, 15)
print(a)

# 4.remove() :delete the first matching items

'''a.remove(50)
print(a)'''  

# 5.pop()    :delete the items and returns also

'''x = a.pop(2)
print(x)        
print(a)'''  

# 6.clear()  :delete all list items

'''b = [1, 2, 3]
b.clear()
print(b) '''

# 7.index()  :show the indexes of the inserting value

'''c = [5, 8, 9]
print(c.index(8))'''

# 8.count()  :count the inserted value how much time

'''d = [1, 2, 2, 3]
print(d.count(2))'''

# 9.sort()   :sorting the list

'''e = [4, 1, 3]
e.sort()
print(e)'''  

# 10.reverse():reverse the list
'''e=[2,4,6,7]
e.reverse()
print(e)'''

# 11.copy()  :making shallow copy 

'''f = e.copy()
print(f)''' 