# Day 85 - Maximal Rectangle

## Problem

Given a `rows x cols` binary matrix filled with `0`s and `1`s, find the
largest rectangle containing only `1`s and return its area.

### Example

Input:

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

Output:

6

## Approach

- Treat each row as the base of a histogram.
- Maintain a `heights` array for consecutive `1`s in each column.
- For every row:
  - Increase the height when the current value is `1`.
  - Reset the height to `0` when the current value is `0`.
- For each updated histogram, use a monotonic stack to find the largest
  rectangle.
- Keep track of the maximum area.

The problem is reduced to repeatedly solving the
**Largest Rectangle in Histogram** problem.

## Complexity

- Time Complexity: O(rows × cols)
- Space Complexity: O(cols)

## Platform

LeetCode #85 - Maximal Rectangle
