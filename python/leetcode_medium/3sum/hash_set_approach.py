def threeSum_hash_set(nums):
    """
    Finds all unique triplets in the array that sum to zero using a hash set for faster lookup.
    
    This approach uses a hash set to avoid checking duplicate triplets and reduces unnecessary iterations.

    Time Complexity:
        O(n²): 
        - The outer loop runs 'n' times.
        - For each iteration of the outer loop, we use a hash set and an inner loop running 'n' times, leading to quadratic time complexity.
    
    Space Complexity:
        O(n): 
        - We use a hash set to track numbers we have already seen.
        - This adds linear space complexity in addition to the output space.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    List[List[int]]: A list of unique triplets where the sum of the elements is zero.
    """
    res = set()
    nums.sort()
    
    for i in range(len(nums)):
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add((nums[i], nums[j], complement))
            seen.add(nums[j])
    
    return [list(triplet) for triplet in res]
