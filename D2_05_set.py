dev = set()
test = {'Giri','Mohammed','Rose','Steve'}
cloud = set(['James','Giri','Mohammed','Michael','Steve'])

dev = {'Gopi','Giri','Mohammed','Rose','Steve'}

dev.add('Jackson')

print(dev)  # {'Giri', 'Rose', 'Mohammed', 'Steve', 'Gopi', 'Jackson'}
dev.add('Giri')  # adding duplicate element, set will not allow duplicates
print(dev)  # {'Giri', 'Rose', 'Mohammed', 'Steve', 'Gopi', 'Jackson'}
l1 = [1,2,3,4,5,1,2,3,11,12,13,11,12,13]
print(len(l1))  # 14 - length of the list
d1 = set([1,2,3,4,5,1,2,3,11,12,13,11,12,13])
print(len(d1))
print(d1)
d1.add(100)
print(d1)  # {1, 2, 3, 4, 5, 11, 12, 13, 100}
d1.remove(100)
d1.discard(100)  # remove element, if not present it will not raise an error
print(d1)
d1.pop()  # remove and return an arbitrary element
print(d1)
d1.discard(2)
print(d1)
d1.discard(2)
# d1.remove(2)  # this will raise an error if 2 is not present
print(d1)

# set operations : union, intersection, difference, symmetric difference


# test = {'Giri','Mohammed','Rose','Steve'}
# cloud = set(['James','Giri','Mohammed','Michael','Steve'])

# dev = {'Gopi','Giri','Mohammed','Rose','Steve'}
# union - merging the two sets, remove duplicates

newset = dev.union(test)  # dev | test
print(newset)  # {'Giri', 'Rose', 'Mohammed', 'Steve', 'Gopi', 'Jackson', 'James'}  

# commin elements in both sets -> 
commonset = dev.intersection(test)  # dev & test -> each element present in both sets
print(commonset)  

ocs = dev & test & cloud  # common elements in dev, test, and cloud
print(ocs)  # {'Giri', 'Mohammed', 'Steve'}

# difference - elements in dev but not in test
onlytest = test.difference(cloud) # test - cloud 
print(onlytest)  # {'rose'}

onlytesting = test - dev - cloud  # test - dev - cloud
print(onlytesting)  # {'rose'}

onlydev = dev - test - cloud
print(onlydev)  # {'Gopi', 'Jackson'}

#  union -> set1 union set2  or set1 | set2
# intersection -> set1 intersection set2  or set1 & set2
# difference -> set1 difference set2  or set1 - set2
