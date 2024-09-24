def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized sliding window approach to find the length of the longest substring without repeating characters.

    Args:
    s (str): Input string consisting of printable ASCII characters.

    Returns:
    int: Length of the longest substring without duplicates.
    
    Time Complexity:
    O(n), where n is the length of the string. Each character is visited once, 
    and the start pointer moves linearly across the string.
    
    Space Complexity:
    O(min(n, m)), where n is the length of the input string and m is the size
    of the character set. Since we're working with ASCII, m is constant (128).
    """
    last_seen = {}
    max_len = 0
    start = 0
    
    # Traverse the string using the 'end' pointer
    for end, char in enumerate(s):
        # If the character has been seen and is within the current window
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        
        # Update the last seen index of the character
        last_seen[char] = end
        
        # Calculate the maximum length of the substring
        max_len = max(max_len, end - start + 1)
    
    return max_len

# Example Usage
s1 = "zyxyzxyz"
s2 = "xxxx"
print(length_of_longest_substring_optimized(s1))  # Output: 3
print(length_of_longest_substring_optimized(s2))  # Output: 1
