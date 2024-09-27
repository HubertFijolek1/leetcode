from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array using binary search with an early exit condition.
        
        Time Complexity:
            - Best Case: O(1) - If the array is already sorted (not rotated), we return the first element.
            - Average/Worst Case: O(log n) - The algorithm uses binary search, dividing the array in half at each step.
        
        Space Complexity: O(1) - Constant extra space is used.

        :param nums: List[int] - The input array which is sorted but rotated.
        :return: int - The minimum element in the array.
        """
        left, right = 0, len(nums) - 1
        
        # Early exit if the array is already sorted
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            # Same logic as before to decide which side has the minimum
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
