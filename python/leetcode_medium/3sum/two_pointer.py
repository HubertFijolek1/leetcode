def threeSum_two_pointer(nums):
    """
    Finds all unique triplets in the array that sum to zero using a two-pointer technique.
    
    This approach leverages sorting and two pointers to reduce the search space for finding valid triplets.

    Time Complexity:
        O(n²): 
        - Sorting the array takes O(n log n).
        - The outer loop runs 'n' times, and for each iteration, the two-pointer search runs in O(n).
        - Overall, this results in a quadratic time complexity.
    
    Space Complexity:
        O(1): 
        - Apart from the space required for storing the result, no additional space is used (excluding the input space).
        - Sorting the array is done in-place, so no extra memory is used.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    List[List[int]]: A list of unique triplets where the sum of the elements is zero.
    """
    res = []
    nums.sort()  # Sorting the array to use two-pointer technique
    
    for i in range(len(nums) - 2):
        # Skip duplicate elements to ensure unique triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                
                # Move left and right pointers and skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    
    return res
