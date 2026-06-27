# Day 29 - Unique Paths

## Problem

A robot starts at the top-left corner of an m × n grid and can only move right or down.

Return the total number of unique paths to reach the bottom-right corner.

### Example

Input:

m = 3
n = 7

Output:

28

## Approach

- Use Dynamic Programming.
- Each cell is the sum of the paths from the top and left cells.
- Optimize space using a 1D DP array.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(n)

## Platform

LeetCode #62 - Unique Paths
