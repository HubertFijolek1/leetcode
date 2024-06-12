def max_subarray(nums):
    """
    Calculates the maximum sum of any contiguous subarray within a given integer array 
    using Kadane's Algorithm.

    This function iterates through the input list `nums` and dynamically calculates 
    the maximum subarray sum. It uses two variables: `cur_sum` to keep the current 
    subarray sum and `max_sum` to store the maximum sum found.
    
    Methodology:
    - Start with `max_sum` initialized to the first element of the array and `cur_sum`
      set to zero.
    - Traverse each number `n` in the array:
      - If `cur_sum` is negative, reset it to zero (ignoring the current subarray since
        adding to it would decrease the potential maximum sum found later).
      - Add `n` to `cur_sum`.
      - Update `max_sum` with the larger of `max_sum` and `cur_sum`.
    - The result is that `max_sum` will contain the maximum sum of any contiguous subarray
      by the end of the loop.

    Time Complexity: O(n), where n is the number of elements in `nums`.
    Space Complexity: O(1), as it uses a constant amount of space regardless of the input size.
    
    Parameters:
    - nums (List[int]): A list of integers representing the array in which to find the maximum
      subarray sum.

    Returns:
    - int: The maximum sum of any contiguous subarray within `nums`.
    
    Example:
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        Answer:  6  # Maximum sum of the subarray [4, -1, 2, 1]

    Note: If the input array `nums` is None, the function returns None.
    """
    if nums is None:
        return None
    
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum
