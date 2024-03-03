def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid 
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  


my_sorted_list = [1, 2, 4, 5, 7, 8, 9]
target_value = 7

result = binary_search(my_sorted_list, target_value)

if result != -1:
    print(f'Target value {target_value} found at index {result}.')
else:
    print(f'Target value {target_value} not found in the list.')
