from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Linear search through the array to find the target.

        Time Complexity: O(n) - We traverse the entire array in the worst case.
        Space Complexity: O(1) - No additional space is used.
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
