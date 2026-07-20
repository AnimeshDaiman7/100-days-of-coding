# Day 52 - Find All Anagrams in a String

## Problem

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

You may return the answer in any order.

### Example

Input:

s = "cbaebabacd"

p = "abc"

Output:

[0,6]

## Approach

- Create two frequency arrays of size 26:
  - One for string `p`.
  - One for the current sliding window in `s`.
- Initialize both arrays using the first window.
- Slide the window across `s`:
  - Add the new character.
  - Remove the leftmost character.
- Compare both frequency arrays.
- If they are equal, store the starting index.

This ensures every possible window is checked only once.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #438 - Find All Anagrams in a String
