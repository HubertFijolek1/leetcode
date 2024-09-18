def is_palindrome_two_pointers(s: str) -> bool:
    """
    Determines if the given string is a palindrome using a two-pointer approach.

    This method uses two pointers starting at both ends of the string, skipping
    non-alphanumeric characters, and comparing characters while moving inward.

    Args:
        s (str): Input string to check if it is a palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity:
        O(n): We iterate over the string once with two pointers where `n` is the length
        of the input string.

    Space Complexity:
        O(1): The algorithm uses only a constant amount of extra space regardless of 
        the input size since we don't create any new strings.

    Example:
        >>> is_palindrome_two_pointers("Was it a car or a cat I saw?")
        True
        >>> is_palindrome_two_pointers("tab a cat")
        False
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True
