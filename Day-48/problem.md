# Day 48 - Subarray Sum Equals K

## Problem

Given an integer array `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

### Example

Input:
nums = [1,1,1], k = 2

Output:
2

## Approach

- Maintain a running prefix sum.
- Use a hash map to store the frequency of each prefix sum.
- For each element:
  - Update the current prefix sum.
  - Check if `(current_sum - k)` exists in the hash map.
  - If it does, add its frequency to the answer.
  - Store the current prefix sum in the hash map.

This efficiently counts all valid subarrays in one pass.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #560 - Subarray Sum Equals K
