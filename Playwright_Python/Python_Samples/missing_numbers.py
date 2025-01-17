def find_missing_num(lst):
    full_range = set(range(min(lst),max(lst)+1))
    print(full_range)
    input_set = set(lst)
    print(input_set)
    missing_numbers = full_range - input_set
    return sorted(missing_numbers)

numbers = [0,1,3,5,6]
missing = find_missing_num(numbers)
print(missing)

