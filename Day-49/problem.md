# Day 49 - Number of Islands

## Problem

Given an `m x n` 2D binary grid representing a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

### Example

Input:

grid =
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output:

1

## Approach

- Traverse every cell in the grid.
- If a land cell (`'1'`) is found:
  - Increase the island count.
  - Perform DFS to mark all connected land cells as visited.
- Continue until the entire grid has been explored.

Each island is visited exactly once.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n) (DFS recursion stack in the worst case)

## Platform

LeetCode #200 - Number of Islands
