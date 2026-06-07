# Day 9 - Merge Intervals

## Problem

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.

### Example

Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

## Approach

- Sort intervals based on starting time.
- Traverse the intervals.
- If the current interval overlaps with the previous one, merge them.
- Otherwise, add it to the result.

## Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Platform

LeetCode #56 - Merge Intervals
