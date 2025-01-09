def find_missing_num(nums):
    n = len(nums)+1
    expected_sum = n*(n+1)//2
    print(expected_sum)
    actual_sum = sum(nums)
    print(actual_sum)
    return expected_sum - actual_sum


nums = [1,2,3,5,6]
missing_nums = find_missing_num(nums)
print(f"Missing Number is: {missing_nums}")