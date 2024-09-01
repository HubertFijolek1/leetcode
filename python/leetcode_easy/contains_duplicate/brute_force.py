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


print(contains_duplicate_bf(list_without_duplicates))  # Output: False
print(contains_duplicate_bf(list_with_duplicates))     # Output: True

