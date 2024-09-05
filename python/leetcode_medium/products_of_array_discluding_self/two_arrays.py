def product_except_self_two_arrays(nums):
    """
    Calculate the product of all elements in the array except the current element using two auxiliary arrays.
    
    Args:
    nums (List[int]): The input list of integers.
    
    Returns:
    List[int]: A list where each element is the product of all other elements except itself.
    
    Complexity:
    Time: O(n) - where n is the length of the input list.
    Space: O(n) - for the two additional arrays used to store left and right products.
    """
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n
    
    # Build left products
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Build right products
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    # Construct the output array using left and right products
    for i in range(n):
        output[i] = left[i] * right[i]
    
    return output

# Test the function with the given examples
print(product_except_self_two_arrays([1, 2, 4, 6]))  # Output: [48, 24, 12, 8]
print(product_except_self_two_arrays([-1, 0, 1, 2, 3]))  # Output: [0, -6, 0, 0, 0]
