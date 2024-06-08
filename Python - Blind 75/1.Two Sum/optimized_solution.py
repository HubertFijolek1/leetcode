def two_sum_hash_table(nums, target):
    """
    An optimized solution to the Two Sum problem using a hash table to store numbers and their indices for quick lookup.
    
    
    Args:
    nums (List[int]): The list of integers.
    target (int): The target sum.
    
    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None
