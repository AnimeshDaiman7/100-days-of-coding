# Day 61 - Minimum Window Substring

## Problem

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.

If there is no such substring, return an empty string.

### Example

Input:

s = "ADOBECODEBANC"

t = "ABC"

Output:

"BANC"

Explanation:

"BANC" is the smallest substring containing all characters of "ABC".

## Approach

- Store the frequency of characters in `t`.
- Use a sliding window with two pointers.
- Expand the window until it contains all required characters.
- Once valid, shrink the window from the left while maintaining validity.
- Track the smallest valid window found.

## Complexity

- Time Complexity: O(m + n)
- Space Complexity: O(k)

where `k` is the number of unique characters.

## Platform

LeetCode #76 - Minimum Window Substring
