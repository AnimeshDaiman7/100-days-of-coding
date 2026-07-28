# Day 60 - Perfect Squares

## Problem

Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A perfect square is an integer that is the square of another integer.

### Example

Input:

n = 12

Output:

3

Explanation:

12 = 4 + 4 + 4

### Example

Input:

n = 13

Output:

2

Explanation:

13 = 4 + 9

## Approach

- Create a DP array where `dp[i]` stores the minimum number of perfect squares needed to make `i`.
- Initialize `dp[0] = 0`.
- For every number from `1` to `n`:
  - Try every perfect square less than or equal to the current number.
  - Update the minimum count.
- Return `dp[n]`.

## Complexity

- Time Complexity: O(n × √n)
- Space Complexity: O(n)

## Platform

LeetCode #279 - Perfect Squares
