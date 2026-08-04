# Day 67 - Sliding Window Maximum

## Problem

Given an integer array `nums` and an integer `k`, return the maximum value in every sliding window of size `k`.

### Example

Input:

nums = [1,3,-1,-3,5,3,6,7]

k = 3

Output:

[3,3,5,5,6,7]

## Approach

- Use a deque to store indices of useful elements.
- Remove indices that fall outside the current window.
- Remove smaller elements from the back of the deque.
- Insert the current index.
- Once the first window is complete, the front of the deque is the maximum.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(k)

## Platform

LeetCode #239 - Sliding Window Maximum
