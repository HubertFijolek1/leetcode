list_without_duplicates = [1,5,3,6,2,77]
list_with_duplicates = [1,5,3,6,2,77,4,3,2]

def contains_duplicate_bf(numbers):
    '''
    Complexity: O(n2) 
    Explanation: This method uses two nested loops to compare each pair of elements 
    in the list. The outer loop runs 𝑛 n times and the inner loop runs from the current
    index of the outer loop to the end of the list, leading to a quadratic number of 
    comparisons.
    '''
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

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

def contains_duplicate_set(numbers):
    '''
    Complexity: O(n) 
    Explanation: This method creates a set from the list and compares the length of the set
    with the length of the list. Creating a set from a list typically involves iterating 
    through all elements and inserting them into the set, which takes O(n) time in the
    average case.
    '''
    return False if len(set(numbers)) == len(numbers) else True

print(contains_duplicate_bf(list_without_duplicates))  # Output: False
print(contains_duplicate_bf(list_with_duplicates))     # Output: True

print(contains_duplicate_sort(list_without_duplicates))  # Output: False
print(contains_duplicate_sort(list_with_duplicates))     # Output: True

print(contains_duplicate_hashmap(list_without_duplicates))  # Output: False
print(contains_duplicate_hashmap(list_with_duplicates))     # Output: True

print(contains_duplicate_set(list_without_duplicates))  # Output: False
print(contains_duplicate_set(list_with_duplicates))     # Output: True
