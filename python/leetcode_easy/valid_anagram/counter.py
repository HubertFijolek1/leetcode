from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams by comparing character counts using a Counter.

        Time Complexity:
        - Counting the characters in both strings takes O(n) time, where n is the length
          of the strings.
        - Comparing the two Counter objects also takes O(n) time, though this is generally
          faster than sorting.

        Space Complexity:
        - The space complexity is O(1) because the Counter object only needs to store
          up to 26 key-value pairs (one for each letter in the alphabet).
        - Even though we are technically using O(n) space to store the frequency counts,
          since the character set is fixed (lowercase English letters), this can be considered O(1).
        """
        return Counter(s) == Counter(t)
    
