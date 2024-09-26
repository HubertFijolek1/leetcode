def validate_parentheses_brute(s: str) -> bool:
    """
    Brute force approach to validate parentheses.
    
    Args:
    s (str): The input string containing brackets.
    
    Returns:
    bool: True if the parentheses are valid, False otherwise.
    
    Time Complexity: O(n^2)
    - For each closing bracket, we search for its corresponding open bracket from the stack, leading to O(n^2).
    
    Space Complexity: O(n)
    - In the worst case, all brackets could be added to a stack.
    """
    stack = []
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s