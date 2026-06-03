# Day 5 - Top K Frequent Elements

## Problem

Given an integer array nums and an integer k, return the k most frequent elements.

### Example

Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]

## Approach

- Count the frequency of each element using a hash map.
- Sort elements based on frequency.
- Return the top k frequent elements.

## Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Platform

LeetCode #347 - Top K Frequent Elements
