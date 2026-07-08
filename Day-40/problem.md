# Day 40 - Squares of a Sorted Array

## Problem

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Example

Input:

nums = [-4,-1,0,3,10]

Output:

[0,1,9,16,100]

## Approach

- Initialize two pointers:
  - Left at the beginning.
  - Right at the end.
- Compare the absolute values of both pointers.
- Place the larger square at the current end of the result array.
- Move the corresponding pointer.
- Repeat until all elements are processed.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #977 - Squares of a Sorted Array
