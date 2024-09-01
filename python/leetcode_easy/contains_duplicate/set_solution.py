list_without_duplicates = [1,5,3,6,2,77]
list_with_duplicates = [1,5,3,6,2,77,4,3,2]


def contains_duplicate_set(numbers):
    '''
    Complexity: O(n) 
    Explanation: This method creates a set from the list and compares the length of the set
    with the length of the list. Creating a set from a list typically involves iterating 
    through all elements and inserting them into the set, which takes O(n) time in the
    average case.
    '''
    return False if len(set(numbers)) == len(numbers) else True


print(contains_duplicate_set(list_without_duplicates))  # Output: False
print(contains_duplicate_set(list_with_duplicates))     # Output: True