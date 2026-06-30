# Day 32 - Longest Substring Without Repeating Characters

## Problem

Given a string `s`, return the length of the longest substring without repeating characters.

### Example

Input:
s = "abcabcbb"

Output:
3

Explanation:
The longest substring without repeating characters is "abc", which has length 3.

## Approach

- Maintain a sliding window using two pointers.
- Store characters inside a Hash Set.
- If a duplicate is found, remove characters from the left until the duplicate is gone.
- Update the maximum window length during traversal.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(min(n, charset))

## Platform

LeetCode #3 - Longest Substring Without Repeating Characters
