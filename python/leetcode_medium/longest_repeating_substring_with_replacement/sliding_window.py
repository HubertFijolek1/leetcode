from collections import defaultdict

def characterReplacementSlidingWindow(s: str, k: int) -> int:
    """
    Finds the length of the longest substring that can be made uniform by replacing up to k characters.
    
    Approach:
    - Uses a sliding window technique to efficiently find the longest valid substring.
    - Expands the window by moving the right pointer and dynamically tracks the frequency of characters in the window.
    - If the number of replacements required exceeds k, shrinks the window by moving the left pointer.
    
    Time Complexity: O(n)
        - Only passes through the string once with the right pointer.
        - The left pointer is only adjusted as needed, ensuring linear time.

    Space Complexity: O(n)
        - Uses extra space for the frequency dictionary to store character counts.
    
    Parameters:
    - s: A string consisting of uppercase English characters.
    - k: The maximum number of allowed replacements.

    Returns:
    - The length of the longest substring that can be made uniform.
    """
    count = defaultdict(int)
    max_len = 0
    max_freq = 0  # Tracks the frequency of the most frequent character in the window
    left = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        
        # If the number of replacements required exceeds k, shrink the window
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
