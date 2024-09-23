def max_area_brute_force(height):
    """
    Calculate the maximum water area using the brute force approach.
    
    The brute force approach checks all possible pairs of bars (i, j),
    and calculates the area of water trapped between them. It uses
    two nested loops to achieve this.

    Time Complexity: O(n^2) - Two nested loops where n is the length of the array.
    Space Complexity: O(1) - Only constant space used.

    Args:
    height (List[int]): A list of integers representing the height of the bars.

    Returns:
    int: The maximum area of water that can be trapped.
    """
    n = len(height)
    max_area = 0
    
    # Check every possible pair of heights
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the area between i and j
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    
    return max_area

heights = [1, 7, 2, 5, 4, 7, 3, 6]
print(max_area_brute_force(heights))  # Output: 36
