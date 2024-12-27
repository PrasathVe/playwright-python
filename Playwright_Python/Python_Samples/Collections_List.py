# List
ls_value = [67,45,34,23,78]
ls_String = ["Yellow","Green","Red"]
print(ls_value[3])#index value of ls_value
ls_value.append(89)#adds value at the end
ls_value.insert(3,88)#insert a value in a particular index
ls_value[0]=11# replace a value from an index
ls_value.pop(0)# removes the specific index value
ls_value.pop()#remove the last index value
ls_value.extend(ls_String)
print(ls_value)
