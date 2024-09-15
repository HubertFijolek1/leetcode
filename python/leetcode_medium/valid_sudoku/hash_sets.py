from collections import defaultdict

def isValidSudoku(board):
    """
    Validates a Sudoku board by using hash sets to track duplicates.
    
    This method uses hash sets to store the digits present in each row, column, 
    and 3x3 sub-box. It checks for duplicates in a single pass through the board. 
    Returns True if the board is valid, and False otherwise.
    
    Time Complexity: O(1) since the board size is fixed at 9x9.
    Space Complexity: O(1) since the board size is constant, but we use extra space
    for hash sets that store digits.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :return: Boolean value indicating whether the Sudoku board is valid.
    """
    
    # Dictionaries to track the digits in rows, columns, and sub-boxes
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # keys for 3x3 sub-boxes are (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            # Check if the current digit already exists in the row, column, or sub-box
            if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                return False
            
            # Add the digit to the respective row, column, and sub-box
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True
