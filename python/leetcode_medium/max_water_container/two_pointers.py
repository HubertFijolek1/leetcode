def max_area_two_pointer(height):
    """
    Calculate the maximum water area using the two-pointer approach.
    
    The two-pointer approach optimizes the brute force approach by only
    considering the largest areas possible, and moving the shorter pointer
    inward to try and find larger potential containers.

    Time Complexity: O(n) - A single pass with two pointers.
    Space Complexity: O(1) - Constant space used.

    Args:
    height (List[int]): A list of integers representing the height of the bars.

    Returns:
    int: The maximum area of water that can be trapped.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the area between left and right
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        
        # Move the shorter pointer inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

heights = [1, 7, 2, 5, 4, 7, 3, 6]
print(max_area_two_pointer(heights))  # Output: 36
