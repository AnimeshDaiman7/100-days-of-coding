# Day 51 - Pacific Atlantic Water Flow

## Problem

There is an `m x n` rectangular island that borders both the Pacific and Atlantic Oceans.

The Pacific Ocean touches the left and top edges of the island, while the Atlantic Ocean touches the right and bottom edges.

Given an integer matrix `heights`, where `heights[r][c]` represents the height of each cell, determine all coordinates from which water can flow to both oceans.

### Example

Input:

heights =
[
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]

Output:

[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

## Approach

- Create two visited sets:
  - Pacific
  - Atlantic
- Run DFS from:
  - Top row and left column (Pacific)
  - Bottom row and right column (Atlantic)
- During DFS, move only to neighboring cells with height greater than or equal to the current cell.
- The intersection of both visited sets gives the answer.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

## Platform

LeetCode #417 - Pacific Atlantic Water Flow
