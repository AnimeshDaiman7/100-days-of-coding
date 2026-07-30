# Day 62 - Container With Most Water

## Problem

Given an integer array `height` of length `n`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container capable of holding the maximum amount of water.

Return the maximum amount of water the container can store.

### Example

Input:

height = [1,8,6,2,5,4,8,3,7]

Output:

49

Explanation:

The container formed by the lines at indices 1 and 8 holds the maximum area of 49.

## Approach

- Initialize two pointers:
  - Left at the beginning.
  - Right at the end.
- Compute the current area.
- Update the maximum area.
- Move the pointer pointing to the shorter line inward.
- Continue until both pointers meet.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #11 - Container With Most Water
