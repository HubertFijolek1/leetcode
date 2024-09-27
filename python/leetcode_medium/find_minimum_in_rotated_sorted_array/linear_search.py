from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array using linear search.
        
        Time Complexity: O(n) - The algorithm iterates through each element in the array once.
        Space Complexity: O(1) - Constant extra space is used.

        :param nums: List[int] - The input array which is sorted but rotated.
        :return: int - The minimum element in the array.
        """
        min_val = nums[0]
        for num in nums:
            if num < min_val:
                min_val = num
        return min_val
