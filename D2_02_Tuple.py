#  collection of data, not going to change, remove duplicates
# DAYS = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# DAYS.append('HOLIDAY')  # add an element to the end of the list
# print(DAYS)  # ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'HOLIDAY']
# DAYS.insert(3,'FRIDAY')  # insert an element at index 3
# print(DAYS)  # ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'FRIDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'HOLIDAY']

# TUPLES: Immutable, Ordered

# list1 = list() => []
# list1 = [1,2,3,4,5]       - list

days = tuple()  # empty tuple - ()
print(days)  # ()

days = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')  # tuple of strings
print(days)
print(days[3])  # THURSDAY
# days[3] = 'Funday'  # this will raise an error, tuples are immutable
month = (1,2,3,4,5)
print(month)  # (1, 2, 3, 4, 5)
# month = (1,2,3,4,5,6,7,8,9,10,11,12)  # tuple of integers
# print(month)
month = (1,2,3,4,5,6,7,8,9,10,11,12)  # tuple of integers
print(len(month))  # 12 - length of the tuple
# month.append(13)  # this will raise an error, tuples are immutable

month = month + (13,)  # adding an element to the tuple
print(month)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

dummy = (14,15,16)
month = month + dummy  # adding another tuple to the existing tuple
print(month)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

l_month = list(month)  # converting tuple to list
l_month[3] = 40
month = tuple(l_month)  # converting list back to tuple
print(month)  # (1, 2, 3, 40, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

print(max(month))  # 40 - maximum value in the tuple
print(min(month))  # 1 - minimum value in the tuple
print(sum(month))  # 195 - sum of all elements in the tuple
l1 = sorted(month) # return list
print(l1)

month = ()
print(month)  # () - empty tuple
del month  # deleting the tuple variable
# print(month)  # this will raise an error, month is not defined