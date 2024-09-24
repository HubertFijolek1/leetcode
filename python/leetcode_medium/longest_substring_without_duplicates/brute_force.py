def length_of_longest_substring_brute_force(s: str) -> int:
    """
    Brute force approach to find the length of the longest substring without repeating characters.

    Args:
    s (str): Input string consisting of printable ASCII characters.

    Returns:
    int: Length of the longest substring without duplicates.
    
    Time Complexity:
    O(n^3), where n is the length of the string. There are O(n^2) substrings,
    and each substring is checked for duplicates in O(n).
    
    Space Complexity:
    O(n), for storing the substrings.
    """
    def has_duplicates(substring):
        return len(set(substring)) != len(substring)

    max_len = 0
    n = len(s)
    
    # Generate all possible substrings and check for duplicates
    for i in range(n):
        for j in range(i, n):
            if not has_duplicates(s[i:j + 1]):
                max_len = max(max_len, j - i + 1)
    
    return max_len

# Example Usage
s1 = "zyxyzxyz"
s2 = "xxxx"
print(length_of_longest_substring_brute_force(s1))  # Output: 3
print(length_of_longest_substring_brute_force(s2))  # Output: 1
