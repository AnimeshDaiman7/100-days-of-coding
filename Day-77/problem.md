# Day 77 - Sudoku Solver

## Problem

Write a program to solve a Sudoku puzzle by filling the empty cells.

A Sudoku solution must satisfy all of the following rules:

1. Each digit `1-9` must occur exactly once in each row.
2. Each digit `1-9` must occur exactly once in each column.
3. Each digit `1-9` must occur exactly once in each of the 9 `3x3`
   sub-boxes.

The `.` character represents an empty cell.

### Example

Input:

[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

The board is solved by filling every empty cell while maintaining
all Sudoku constraints.

## Approach

The solution uses Backtracking.

- Find an empty cell.
- Try every digit from `1` to `9`.
- Check whether the digit is valid in:
  - The current row.
  - The current column.
  - The current `3x3` sub-box.
- If the digit is valid, place it in the cell.
- Recursively solve the remaining board.
- If the recursive solution fails, remove the digit and try another one.
- Continue until there are no empty cells.

## Complexity

- Time Complexity: O(9^m), where `m` is the number of empty cells.
- Space Complexity: O(m) for the recursion stack.

## Platform

LeetCode #37 - Sudoku Solver
