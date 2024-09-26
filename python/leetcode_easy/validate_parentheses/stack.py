def validate_parentheses_stack(s: str) -> bool:
    """
    Stack-based approach to validate parentheses.
    
    Args:
    s (str): The input string containing brackets.
    
    Returns:
    bool: True if the parentheses are valid, False otherwise.
    
    Time Complexity: O(n)
    - We iterate through the string once, and each push/pop operation is O(1).
    
    Space Complexity: O(n)
    - We use a stack that may grow up to the size of the input string in the worst case.
    """
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack
