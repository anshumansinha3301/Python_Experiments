def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i 
    return -1 

my_list = [4, 2, 8, 1, 7, 5, 9]
target_value = 7

result = linear_search(my_list, target_value)

if result != -1:
    print(f'Target value {target_value} found at index {result}.')
else:
    print(f'Target value {target_value} not found in the list.')
 
