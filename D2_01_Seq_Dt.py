# store a set of elements in a variable

# order
# index
# divide from 0 to n
# iterate
# modify - mutable
# modify

# list : ordered, allow duplicates, mutable, add, remove, change elements -> LIST

list1 = ['apple', 'banana', 'cherry']  # list of strings
#         0        1          2
# access with index, index start from 0
print(list1[0])  # apple
list1.append('apple')       # add at the end
print(list1)

list2 = [1,2,3,4,5]  # list of integers
list3 = list()  # empty list with list constructor
print(list3)  # empty list
print(type(list3))  # <class 'list'>
list1.insert(1,'cherry')  # insert at index 1
print(list1)  # ['apple', 'cherry', 'banana', 'cherry', 'apple']

print(list2)  # [1, 2, 3, 4, 5]
list2.extend(list1)
print(list2)  # [1, 2, 3, 4, 5, 'apple', 'cherry', 'banana', 'cherry', 'apple']


list1.append('strawberry')  # add at the end
print(list1)  # ['apple', 'cherry', 'banana', 'cherry

# list1.append('kiwi','orange')  # this will raise an error, append takes only one argument
# print(list1)  # ['apple', 'cherry', 'banana', 'cherry

list1.extend(['papaya','grapes','musambi'])  # add multiple elements at the end
print(list1)  # ['apple', 'cherry', 'banana', 'cherry', 'apple', 'strawberry', 'papaya', 'grapes', 'musambi']

print(list2)
list2.pop()  # remove the last element
print(list2)  # [1, 2, 3, 4, 5, 'apple', 'cherry', 'banana', 'cherry']
print(list2.count('cherry'))
list2.remove('cherry')
print(list2)
print(len(list2))  # length of the list, no of elements in the list
name = 'Giri Prasad'
print('no of char in name is ', len(name))  # length of the string

list2.pop() # remove the last element
print(list2)  
list2.pop(5)  # remove the element at index 5, apple removed
print(list2) 

list2.clear()
print(list2)  # [] - empty list
del name  # delete the variable name
# print(name)

del list2  # delete the list2 variable
# print(list2)
del list1, list3  # delete multiple variables