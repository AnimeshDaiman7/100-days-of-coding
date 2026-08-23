# Day 84 - N-Queens II

## Problem

Given an integer `n`, return the number of distinct solutions to the
n-queens puzzle.

The goal is to place `n` queens on an `n x n` chessboard such that no two
queens attack each other.

### Example

Input:

n = 4

Output:

2

There are two distinct solutions for the 4-queens puzzle.

## Approach

Use Backtracking to place one queen in each row.

For every row:

- Try every column.
- Check whether the column is already occupied.
- Check both diagonals.
- If the position is valid, place the queen and move to the next row.
- After exploring that choice, remove the queen and try another position.

Three sets are used for efficient checking:

- `cols` stores occupied columns.
- `diag1` stores `row - col`.
- `diag2` stores `row + col`.

When all `n` rows are successfully filled, increment the solution count.

## Complexity

- Time Complexity: O(N!)
- Space Complexity: O(N)

## Platform

LeetCode #52 - N-Queens II
