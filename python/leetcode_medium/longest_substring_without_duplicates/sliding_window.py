def length_of_longest_substring_sliding_window(s: str) -> int:
    """
    Sliding window approach to find the length of the longest substring without repeating characters.

    Args:
    s (str): Input string consisting of printable ASCII characters.

    Returns:
    int: Length of the longest substring without duplicates.
    
    Time Complexity:
    O(n^2), where n is the length of the string. We expand and shrink the window repeatedly.
    
    Space Complexity:
    O(n), for storing the characters in the current window.
    """
    max_len = 0
    n = len(s)
    
    # Sliding window approach
    for i in range(n):
        seen = set()  # Set to track characters in the current window
        for j in range(i, n):
            if s[j] in seen:
                break  # Stop expanding if a duplicate is found
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    
    return max_len

# Example Usage
s1 = "zyxyzxyz"
s2 = "xxxx"
print(length_of_longest_substring_sliding_window(s1))  # Output: 3
print(length_of_longest_substring_sliding_window(s2))  # Output: 1
