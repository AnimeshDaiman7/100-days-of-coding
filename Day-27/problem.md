# Day 27 - Is Subsequence

## Problem

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence is formed by deleting some characters without changing the order of the remaining characters.

### Example

Input:

s = "abc"
t = "ahbgdc"

Output:

true

## Approach

- Use two pointers.
- Traverse string t.
- Whenever characters match, advance pointer in s.
- If all characters of s are matched, return true.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #392 - Is Subsequence
