# Day 34 - House Robber

## Problem

You are given an integer array `nums` representing the amount of money stored in each house.

Adjacent houses cannot be robbed because they have connected security systems.

Return the maximum amount of money you can rob without alerting the police.

### Example

Input:
nums = [2,7,9,3,1]

Output:
12

Explanation:
Rob houses with money 2, 9, and 1.
Total = 12.

## Approach

- Use Dynamic Programming.
- At every house decide whether to:
  - Rob it (previous non-adjacent profit + current money)
  - Skip it (previous maximum profit)
- Store only the previous two results to achieve O(1) space.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #198 - House Robber
