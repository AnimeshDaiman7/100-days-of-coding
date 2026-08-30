# Day 91 - Spiral Matrix

## Problem

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Example

Input:

matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output:

[1,2,3,6,9,8,7,4,5]

## Approach

- Maintain four boundaries:
  - `top`
  - `bottom`
  - `left`
  - `right`
- Traverse the top row from left to right.
- Traverse the right column from top to bottom.
- Traverse the bottom row from right to left.
- Traverse the left column from bottom to top.
- Move the boundaries inward after each traversal.
- Continue until all elements are visited.
- Check the boundaries before traversing the bottom row and left column to
  handle single-row or single-column cases.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(1) excluding the output array

## Platform

LeetCode #54 - Spiral Matrix
