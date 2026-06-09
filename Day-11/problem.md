# Day 11 - Maximum Subarray

## Problem

Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

### Example

Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6

Explanation:
The subarray [4,-1,2,1] has the largest sum.

## Approach

- Use Kadane's Algorithm.
- At each position, decide whether to:
  - Start a new subarray.
  - Extend the current subarray.
- Keep track of the maximum sum seen so far.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #53 - Maximum Subarray
