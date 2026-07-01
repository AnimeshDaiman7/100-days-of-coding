# Day 33 - Island Perimeter

## Problem

You are given a grid where `1` represents land and `0` represents water.

Return the perimeter of the island.

### Example

Input:
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

Output:
16

## Approach

- Traverse every cell in the grid.
- Every land cell initially contributes 4 sides.
- If the upper neighbor is land, subtract 2.
- If the left neighbor is land, subtract 2.
- Return the final perimeter.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(1)

## Platform

LeetCode #463 - Island Perimeter
