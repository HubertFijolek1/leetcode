def product_except_self(nums):
    #time complexity O(n)
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    answer = [1] * n
    
    # Compute left products
    for i in range(1, n):
        # Example: left_products[1] = left_products[0] * nums[0] = 1 * 1 = 1
        #          left_products[2] = left_products[1] * nums[1] = 1 * 2 = 2
        #          left_products[3] = left_products[2] * nums[2] = 2 * 3 = 6
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    # Compute right products
    for i in range(n - 2, -1, -1):
        # Example: right_products[2] = right_products[3] * nums[3] = 1 * 4 = 4
        #          right_products[1] = right_products[2] * nums[2] = 4 * 3 = 12
        #          right_products[0] = right_products[1] * nums[1] = 12 * 2 = 24
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    # Fill the answer array
    for i in range(n):
        # Example: answer[0] = left_products[0] * right_products[0] = 1 * 24 = 24
        #          answer[1] = left_products[1] * right_products[1] = 1 * 12 = 12
        #          answer[2] = left_products[2] * right_products[2] = 2 * 4 = 8
        #          answer[3] = left_products[3] * right_products[3] = 6 * 1 = 6
        answer[i] = left_products[i] * right_products[i]
    
    return answer

# Example list
example_list = [1, 2, 3, 4]
print(product_except_self(example_list))  # Output should be [24, 12, 8, 6]
