from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams using a defaultdict to count character frequencies.

        Time Complexity:
        - O(n), where n is the length of the strings. We loop through each string once.

        Space Complexity:
        - O(1), because we use a fixed-size defaultdict that stores up to 26 keys,
          which corresponds to the lowercase English letters. This space usage is constant.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        
        if len(s) != len(t):
            return False
        
        # Initialize a defaultdict where missing keys are automatically initialized to 0
        count = defaultdict(int)
        
        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            # If the count for any character goes below 0, t has more of this character than s
            if count[char] < 0:
                return False
        
        # If all values in the dictionary are zero, the strings are anagrams
        return True
