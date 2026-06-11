# Day 13 - Product of Array Except Self

## Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must solve it without using division and in O(n) time.

### Example

Input:
nums = [1,2,3,4]

Output:
[24,12,8,6]

## Approach

- Calculate prefix products from left to right.
- Calculate postfix products from right to left.
- Multiply prefix and postfix values for each index.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1) extra space (excluding output array)

## Platform

LeetCode #238 - Product of Array Except Self
