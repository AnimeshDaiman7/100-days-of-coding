# Day 76 - N-Queens

## Problem

The n-queens puzzle is the problem of placing `n` queens on an `n x n`
chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle.

Each solution represents a different board configuration where:

- `Q` represents a queen.
- `.` represents an empty space.

### Example

Input:

n = 4

Output:

[
    [".Q..",
     "...Q",
     "Q...",
     "..Q."],

    ["..Q.",
     "Q...",
     "...Q",
     ".Q.."]
]

There are two distinct solutions for `n = 4`.

## Approach

The solution uses Backtracking.

- Place one queen in each row.
- Try every column in the current row.
- Check whether the position is safe.
- If the position is safe, place the queen and move to the next row.
- If no valid position exists, remove the previously placed queen and
  try another position.
- When all rows contain a queen, store the board as a solution.

To check positions efficiently, maintain sets for:

- Columns
- `row - column` diagonals
- `row + column` diagonals

This allows us to determine whether a queen can be placed without
scanning the entire board.

## Complexity

- Time Complexity: O(n!)
- Space Complexity: O(n²)

## Platform

LeetCode #51 - N-Queens
