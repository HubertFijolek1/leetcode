def characterReplacementBruteForce(s: str, k: int) -> int:
    """
    Finds the length of the longest substring that can be made uniform by replacing up to k characters.
    
    Approach:
    - Uses brute force to check every possible substring of the string.
    - For each substring, counts how many characters need to be replaced to make the substring uniform.
    
    Time Complexity: O(n^3)
        - Two nested loops for substring generation (O(n^2)).
        - Counting the most frequent character in each substring takes O(n) for each substring.
    
    Space Complexity: O(1)
        - Uses constant space for storing variables, as no extra space is used apart from the input.

    Parameters:
    - s: A string consisting of uppercase English characters.
    - k: The maximum number of allowed replacements.

    Returns:
    - The length of the longest substring that can be made uniform.
    """
    def canMakeUniform(substring, k):
        max_count = 0
        for char in set(substring):
            count = substring.count(char)
            max_count = max(max_count, count)
        return len(substring) - max_count <= k

    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if canMakeUniform(s[i:j], k):
                max_len = max(max_len, j - i)
    
    return max_len
