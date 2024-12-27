# Do not allow Duplicate, Duplicate value will be over write existing value
# Any type of data can be stored
# Key:value pair {"name":"Mark"}
# get(),keys(),values(),items(),update({""year":"2024"}),thisdict["color"]="red",thisdict.pop("model"),del,
dict_value= {
    "Name":"Apple",
    "Processor":"Intel",
    "Ram":"64 GB"

}
print (dict_value)# Print the entire values
print(dict_value["Name"])# Prints value of specific provided Key
print(dict_value.keys())# Print only the keys
print(dict_value.values())# Print only the values
dict_value ["Color"]="Silver Grey"# Can add a new item (key value pair)
print (dict_value)
# del dict_value will delete the entire dictionary
# dict_value.clear() Clears the complete entries in a dictionary 
