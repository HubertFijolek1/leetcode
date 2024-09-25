from collections import defaultdict

def characterReplacementOptimizedBruteForce(s: str, k: int) -> int:
    """
    Finds the length of the longest substring that can be made uniform by replacing up to k characters.
    
    Approach:
    - Optimizes the brute force approach by dynamically updating the character frequency counts 
      as the window expands.
    
    Time Complexity: O(n^2)
        - One loop for each starting point of the substring (O(n)).
        - An inner loop to expand the window (O(n)).
        - Updating the character frequency takes O(1) for each character.

    Space Complexity: O(n)
        - Uses extra space to store character frequencies in the current window.
    
    Parameters:
    - s: A string consisting of uppercase English characters.
    - k: The maximum number of allowed replacements.

    Returns:
    - The length of the longest substring that can be made uniform.
    """
    max_len = 0
    for i in range(len(s)):
        count = defaultdict(int)
        max_count = 0
        for j in range(i, len(s)):
            count[s[j]] += 1
            max_count = max(max_count, count[s[j]])
            
            # If the number of characters to be replaced is <= k
            if (j - i + 1) - max_count <= k:
                max_len = max(max_len, j - i + 1)
    
    return max_len
