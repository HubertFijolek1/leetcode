def validate_parentheses_optimized(s: str) -> bool:
    """
    Optimized stack approach to validate parentheses.
    
    Args:
    s (str): The input string containing brackets.
    
    Returns:
    bool: True if the parentheses are valid, False otherwise.
    
    Time Complexity: O(n)
    - We scan the string once and perform constant time operations for each character.
    
    Space Complexity: O(n)
    - The size of the stack can grow linearly with the input size in the worst case.
    """
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return not stack
