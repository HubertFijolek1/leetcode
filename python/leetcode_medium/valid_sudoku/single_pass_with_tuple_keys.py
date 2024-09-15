def isValidSudoku(board):
    """
    Optimized solution to validate a Sudoku board using a single-pass approach with tuple keys.
    
    This method tracks the digits in rows, columns, and 3x3 sub-boxes using a single hash set.
    Each element is stored as a tuple consisting of row, column, and sub-box identifiers. 
    This ensures the board is checked for validity in a single pass.
    
    Time Complexity: O(1) since the board size is fixed at 9x9.
    Space Complexity: O(1) since we use fixed space for hash sets to track the digits.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :return: Boolean value indicating whether the Sudoku board is valid.
    """
    
    seen = set()  # Set to track seen digits in rows, columns, and boxes

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            
            # Generate unique keys for row, column, and sub-box
            row_key = (r, num)
            col_key = (num, c)
            box_key = (r // 3, c // 3, num)

            # If any key already exists, the board is invalid
            if row_key in seen or col_key in seen or box_key in seen:
                return False

            # Add the keys to the set to mark the current digit as seen
            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

    return True
