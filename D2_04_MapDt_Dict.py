# word - meaning
# key - value

# dictionary - collection of key-value pairs, 
# mutable, unordered

# dasid: 'a825662'
# 'name': 'Giri Prasad', 'age': 30, 'city': 'Chennai'

d1 = dict()  # empty dictionary {}
d1 = {}
print(type(d1))  # <class 'dict'>
d1 = {'name': 'Giri Prasad', 'age': 30, 'city': 'Chennai'}  # dictionary with key-value pairs
print(d1)  # {'name': 'Giri Prasad', 'age': 30, 'city': 'Chennai'}
print(d1.keys())  # dict_keys(['name', 'age', 'city']) - keys of the dictionary
print(d1.values())  # dict_values(['Giri Prasad', 30, 'Chennai']) - values of the dictionary
d1['age'] = 41
print(d1)  # {'name': 'Giri Prasad', 'age': 41, 'city': 'Chennai'} - updated value for key 'age'
d1['country'] = 'India' # it will check for key 'country', if not found, it will add the key-value pair
print(d1)  # {'name': 'Giri Prasad', 'age': 41, 'city': 'Chennai', 'country': 'India'} - added new key-value pair

print(d1.items())

d1.pop('age')
print(d1)  # {'name': 'Giri Prasad', 'city': 'Chennai', 'country': 'India'} - removed key 'age'

d1.popitem()  # removes the last inserted key-value pair
print(d1)  # {'name': 'Giri Prasad', 'city': 'Chennai'} - removed last key-value pair

d1['age']=''
print(d1)  # {'name': 'Giri Prasad', 'city': 'Chennai', 'age': ''} - added key 'age' with empty value
print(d1.get('age'))  # '' - get value for key 'age', if key not found, it will return None or default value if provided
d1.pop('age')  # remove key 'age'
print(d1)
d1['age'] = 40
print(d1.get('age','Value is missing'))

for keys in d1:
    print(keys, '->', d1[keys])  # iterate through keys and print key-value pairs

for k, v in d1.items():
    print(k,':', v)


dict1 = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'd': 'date', 'e':'papaya'}
dict2 = {'e': '', 'f': 'fig', 'g': 'grape'}

result1 = dict2 | dict1
print(result1)