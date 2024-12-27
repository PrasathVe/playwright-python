#Set {}=> Do no allow Duplicate, Duplicate values will be removed
# Any type of data can be stored
# We cannot modify the set item but we can add or remove items
# Sets are unordered
a={1,3,4,5,6,7}
a.add(34) # Add item
a.remove(3)# Index value needs to be specified
a.update()
a.pop()
print(a)