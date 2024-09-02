from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams from a list of strings using character frequency counting.

        This method creates a list of counts for each letter in the alphabet (assuming
        all strings contain only lowercase English letters). These counts are used as
        a tuple key to group all anagrams together in a dictionary.

        Args:
            strs (List[str]): A list of strings to group by anagrams.

        Returns:
            List[List[str]]: A list of lists, where each sublist contains words that are
            anagrams of each other.

        Time Complexity:
            O(n * k), where:
            - n is the number of strings.
            - k is the average length of the strings.
            The counting of characters in each string takes O(k), and this is done for all n strings.

        Space Complexity:
            O(n * k), where:
            - n is the number of strings.
            - k is the average length of the strings.
            Space is required to store the dictionary keys (tuples of size 26) and the grouped anagrams.

        Example:
            >>> strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
            >>> sol = Solution()
            >>> sol.groupAnagrams(strs)
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        ans = defaultdict(list)

        for s in strs:
            # Create a list to count the frequency of each character in the word
            count = [0] * 26
            for c in s:
                # Increment the count for the corresponding character
                count[ord(c) - ord("a")] += 1
            # Use the tuple of counts as a key in the dictionary
            ans[tuple(count)].append(s)
        
        # Convert the dictionary values to a list of lists and return
        return list(ans.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
