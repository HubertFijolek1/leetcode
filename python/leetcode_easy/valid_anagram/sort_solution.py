class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams by sorting.

        Time Complexity:
        - The sorted() function in Python uses Timsort, which has a best-case and average-case
          time complexity of O(n log n).

        Space Complexity:
        - The space complexity is O(n) because sorted() creates a new list of characters
          from the original string, requiring additional space proportional to the length
          of the string.
        - In total, we need O(n) space for each string, leading to an overall space complexity
          of O(n).
        """
        return sorted(s) == sorted(t)
