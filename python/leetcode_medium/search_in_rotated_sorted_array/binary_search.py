from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search by first identifying the pivot point where the rotation occurs.
        Once the pivot is found, we perform binary search on the correct half of the array.

        Time Complexity: O(log n) - The binary search takes logarithmic time.
        Space Complexity: O(1) - No additional space is used.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Left side is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
