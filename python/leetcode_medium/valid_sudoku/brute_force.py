def isValidSudoku(board):
    """
    Validates a Sudoku board using a brute-force approach.
    
    This method checks all rows, columns, and 3x3 sub-boxes separately
    to ensure no duplicates exist in any of them. The function returns 
    True if the board is valid, and False otherwise.

    Time Complexity: O(1) due to the fixed size of the board (9x9).
    Space Complexity: O(1) as no extra space is needed beyond the input.
    
    :param board: A 9x9 list of lists representing the Sudoku board.
    :return: Boolean value indicating whether the Sudoku board is valid.
    """
    
    # Helper function to check if a group (row, column, or box) is valid
    def isValidGroup(group):
        seen = set()
        for char in group:
            if char != ".":
                if char in seen:
                    return False
                seen.add(char)
        return True

    # Check each row
    for row in board:
        if not isValidGroup(row):
            return False

    # Check each column
    for col in range(9):
        if not isValidGroup([board[row][col] for row in range(9)]):
            return False

    # Check each 3x3 sub-box
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = []
            for x in range(3):
                for y in range(3):
                    sub_box.append(board[i + x][j + y])
            if not isValidGroup(sub_box):
                return False

    return True
