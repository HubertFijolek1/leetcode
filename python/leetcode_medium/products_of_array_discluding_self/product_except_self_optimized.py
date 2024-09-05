def product_except_self_optimized(nums):
    """
    Calculate the product of all elements in the array except the current element using a single auxiliary array.
    
    Args:
    nums (List[int]): The input list of integers.
    
    Returns:
    List[int]: A list where each element is the product of all other elements except itself.
    
    Complexity:
    Time: O(n) - where n is the length of the input list.
    Space: O(1) - if we don't count the output array as additional space; otherwise O(n).
    """
    n = len(nums)
    output = [1] * n
    
    # Build left products directly in the output array
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Build right products directly in the output array
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# Test the function with the given examples
print(product_except_self_optimized([1, 2, 4, 6]))  # Output: [48, 24, 12, 8]
print(product_except_self_optimized([-1, 0, 1, 2, 3]))  # Output: [0, -6, 0, 0, 0]
