list_without_duplicates = [1,5,3,6,2,77]
list_with_duplicates = [1,5,3,6,2,77,4,3,2]

def contains_duplicate_hashmap(numbers):
    '''
    Complexity: O(n) 
    Explanation: This method uses a dictionary (hashmap) to track the occurrences of 
    each number. It performs a single pass through the list, checking each number against
    the dictionary, which offers average-case O(1) time complexity for insert and check
    operations. Thus, the overall time complexity is linear.
    '''
    dict_num = {}
    for i in numbers:
        if i not in dict_num:
            dict_num[i] = i
        else: return True
    return False

print(contains_duplicate_hashmap(list_without_duplicates))  # Output: False
print(contains_duplicate_hashmap(list_with_duplicates))     # Output: True