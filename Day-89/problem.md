# Day 89 - Distinct Subsequences

## Problem

Given two strings `s` and `t`, return the number of distinct subsequences
of `s` which equals `t`.

### Example

Input:

s = "rabbbit"
t = "rabbit"

Output:

3

## Approach

Use Dynamic Programming.

- `dp[j]` represents the number of ways to form the first `j` characters
  of `t`.
- Initially, `dp[0] = 1` because an empty string can always be formed
  by choosing nothing.
- For every character in `s`, process `t` from right to left.
- If the current characters match, we can either:
  - Use the current character.
  - Skip the current character.
- Therefore:

  `dp[j] = dp[j] + dp[j-1]`

- If the characters do not match, no update is required.

Processing from right to left ensures that previous DP values are not
overwritten before they are used.

## Complexity

- Time Complexity: O(n × m)
- Space Complexity: O(m)

where `n = len(s)` and `m = len(t)`.

## Platform

LeetCode #115 - Distinct Subsequences
