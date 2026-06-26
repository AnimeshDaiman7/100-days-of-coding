# Day 28 - Flood Fill

## Problem

Given an image represented as a 2D grid, perform a flood fill starting from the pixel (sr, sc) by replacing all connected pixels having the same original color with the new color.

### Example

Input:

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

Output:

[[2,2,2],[2,2,0],[2,0,1]]

## Approach

- Store the original color.
- If the original color equals the new color, return immediately.
- Perform DFS.
- Visit all four directions.
- Color every connected pixel.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

## Platform

LeetCode #733 - Flood Fill
