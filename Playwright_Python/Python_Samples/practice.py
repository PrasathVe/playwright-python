# Tuple
fruit_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruit_tuple[2:5]) #2 Starting index , 5 Ending Index

#Output : ('cherry', 'orange', 'kiwi') (2,3,4)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# List
mylist = ["Yellow", 76,67.43,"car"]
print(mylist)
sort_list = [100, 50, 65, 82, 23]
print("Before Sort: ",sort_list)
sort_list.sort()
print("After Sort: " ,sort_list)
sort_list.sort(reverse=True)
print("After Sort and revered: ",sort_list)

# Set

# 1 and True will be considered Same as well as 0 and False will be considered same

this_set = {"apple", "banana", "cherry", False, True, 0}
print(this_set)
# Join Sets
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Dictionaries
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)

