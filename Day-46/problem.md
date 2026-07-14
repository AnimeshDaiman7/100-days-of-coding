# Day 46 - Find the Duplicate Number

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`. Return this repeated number.

You must solve the problem without modifying the array and using only constant extra space.

### Example

Input:
nums = [1,3,4,2,2]

Output:
2

## Approach

- Treat the array as a linked list.
- Each value points to the next index.
- Because one number is duplicated, a cycle is formed.
- Use Floyd's Tortoise and Hare algorithm to detect the cycle.
- Find the entrance of the cycle, which represents the duplicate number.

This approach satisfies all problem constraints.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #287 - Find the Duplicate Number
