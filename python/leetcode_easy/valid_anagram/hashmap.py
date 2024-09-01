class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams using a single frequency dictionary.

        Time Complexity:
        - We traverse both strings once, so the time complexity is O(n), where n is the
          length of the strings.

        Space Complexity:
        - The space complexity is O(1) because we are using a single dictionary to track
          character frequencies. Since the maximum number of unique characters is limited
          to 26 (lowercase English letters), this can be considered O(1) space usage.
        - Although in a general case with an arbitrary set of characters it would be O(n),
          here it is effectively constant.
        """
        
        # If the lengths of the strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            # If char is not in the dictionary, get() initializes it to 0
            # Then we add 1 to the count of that character
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            # If the character is not in the dictionary or the count is 0, t has an extra character
            if char not in count or count[char] == 0:
                return False
            # Decrement the count for each character found in t
            count[char] -= 1
        
        # After processing, all counts should be zero if s and t are anagrams
        # If any count is not zero, the strings are not anagrams
        return all(value == 0 for value in count.values())
