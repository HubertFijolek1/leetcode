def two_sum_brute_force(nums, target):
    """
    A brute force solution to the Two Sum problem that checks all pairs of numbers to find two that sum to the target.
    
    Args:
    nums (List[int]): The list of integers.
    target (int): The target sum.
    
    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
