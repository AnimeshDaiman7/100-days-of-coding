# Day 68 - Regular Expression Matching

## Problem

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.

Return `true` if the pattern matches the entire input string.

### Example

Input:

s = "aa"

p = "a*"

Output:

true

Explanation:

`*` means zero or more occurrences of the preceding element `a`, so `"a*"` matches `"aa"`.

## Approach

- Create a DP table.
- Initialize the first row and column.
- If characters match (or pattern contains `.`):
  - Copy the diagonal value.
- If pattern contains `*`:
  - Ignore the previous character.
  - Or match one/more occurrences.
- Return the value in the last DP cell.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

Where:

- m = length of string
- n = length of pattern

## Platform

LeetCode #10 - Regular Expression Matching
