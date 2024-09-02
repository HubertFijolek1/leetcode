from collections import defaultdict

def groupAnagramsSorting(strs):
    """
    Groups anagrams from the given list of strings.
    
    This function sorts each word in the input list and uses the sorted word as a key 
    to group all anagrams together. Anagrams are words that have the same characters 
    in a different order.
    
    Args:
        strs (List[str]): A list of strings to be grouped by anagrams.
    
    Returns:
        List[List[str]]: A list of lists, where each sublist contains words that are anagrams of each other.
    
    Time Complexity:
        O(n * k log k), where:
        - n is the number of words in the input list.
        - k is the average length of each word.
        Sorting each word takes O(k log k) time, and we do this for all n words.

    Space Complexity:
        O(n * k), where:
        - n is the number of words.
        - k is the average length of each word.
        The space complexity includes the storage required for the dictionary and the list of grouped anagrams.

    Example:
        >>> strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        >>> groupAnagramsSorting(strs)
        [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
    """

    anagram_dict = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        # Append the original word to the list corresponding to the sorted key
        anagram_dict[sorted_word].append(word)
    
    return list(anagram_dict.values())

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(groupAnagramsSorting(strs))  # Output: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
