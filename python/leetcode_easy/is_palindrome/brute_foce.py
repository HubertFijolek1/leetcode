def is_palindrome_bruteforce(s: str) -> bool:
    """
    Determines if the given string is a palindrome using a brute-force approach.

    This method removes all non-alphanumeric characters, converts the string to lowercase,
    and checks if the resulting string is equal to its reverse.

    Args:
        s (str): Input string to check if it is a palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity:
        O(n): We iterate over the entire string to filter out non-alphanumeric characters
        and then reverse it, where `n` is the length of the input string.

    Space Complexity:
        O(n): We create a new string that contains only the alphanumeric characters of 
        the input string, which requires O(n) additional space.

    Example:
        >>> is_palindrome_bruteforce("Was it a car or a cat I saw?")
        True
        >>> is_palindrome_bruteforce("tab a cat")
        False
    """
    filtered_chars = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_chars == filtered_chars[::-1]
