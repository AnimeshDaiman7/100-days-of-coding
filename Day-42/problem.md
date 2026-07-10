# Day 42 - Find Smallest Letter Greater Than Target

## Problem

Given a sorted array of characters `letters` and a character `target`, return the smallest character that is lexicographically greater than `target`.

If no such character exists, return the first character in the array.

### Example

Input:
letters = ["c","f","j"]
target = "a"

Output:
"c"

## Approach

- Perform Binary Search on the sorted array.
- Keep track of the smallest character greater than target.
- If none exists, return the first element due to wrap-around.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

## Platform

LeetCode #744 - Find Smallest Letter Greater Than Target
