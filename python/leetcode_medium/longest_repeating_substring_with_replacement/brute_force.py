def characterReplacementBruteForce(s: str, k: int) -> int:
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

# Example usage
s = "AAABABB"
k = 1
print(characterReplacementBruteForce(s, k))  # Output: 5
