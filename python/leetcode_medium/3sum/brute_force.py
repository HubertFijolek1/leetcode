def threeSum_brute_force(nums):
    """
    Finds all unique triplets in the array that sum to zero using a brute force approach.
    
    This method checks every possible triplet combination in the array.

    Time Complexity:
        O(n³): 
        - We have three nested loops over the input array.
        - Each loop runs for 'n' iterations, leading to cubic time complexity.
    
    Space Complexity:
        O(1): 
        - We do not use any additional data structures except the result list.
        - This ignores the space used for storing the output triplets.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    List[List[int]]: A list of unique triplets where the sum of the elements is zero.
    """
    res = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in res:
                        res.append(triplet)
    return res
