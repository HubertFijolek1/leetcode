list_without_duplicates = [1,5,3,6,2,77]
list_with_duplicates = [1,5,3,6,2,77,4,3,2]

def contains_duplicate_sort(numbers):
    '''
    Complexity: O(nlogn) 
    Explanation: First, the list is sorted, which typically takes O(nlogn) time using
    comparison-based sorting algorithms like Timsort (used by Python's built-in sort). 
    After sorting, a single pass through the list (linear scan) checks for consecutive
    duplicate elements, taking O(n) time. The dominant factor here is the sorting step.
    '''
    numbers.sort()
    for i in range(1,len(numbers)):
        if numbers[i-1] == numbers[i]:
            return True
    return False

print(contains_duplicate_sort(list_without_duplicates))  # Output: False
print(contains_duplicate_sort(list_with_duplicates))     # Output: True

