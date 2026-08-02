# Day 65 - Longest Increasing Subsequence

## Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

### Example

Input:

nums = [10,9,2,5,3,7,101,18]

Output:

4

Explanation:

The longest increasing subsequence is [2,3,7,101], so its length is 4.

## Approach

- Maintain a list `tails`.
- Traverse every element in the array.
- If the current number is larger than the last value in `tails`, append it.
- Otherwise, use binary search to replace the first element greater than or equal to the current number.
- The size of `tails` represents the length of the LIS.

## Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Platform

LeetCode #300 - Longest Increasing Subsequence
