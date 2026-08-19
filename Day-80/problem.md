# Day 80 - Wildcard Matching

## Problem

Given an input string `s` and a pattern `p`, implement wildcard pattern
matching with support for `?` and `*`.

- `?` matches any single character.
- `*` matches any sequence of characters, including the empty sequence.

The matching must cover the entire input string.

### Example

Input:

s = "aa"
p = "*"

Output:

true

Explanation:

`*` can match any sequence of characters, including `"aa"`.

## Approach

The solution uses Dynamic Programming.

For every state `(i, j)`, determine whether the substring starting at
`i` in `s` can be matched with the pattern starting at `j` in `p`.

There are three main cases:

1. If the current characters match or `p[j] == '?'`:
   - Move both pointers forward.

2. If `p[j] == '*'`:
   - Treat `*` as matching zero characters and move the pattern pointer.
   - Treat `*` as matching one or more characters and move the string
     pointer.

3. Otherwise:
   - The current characters do not match, so return `false`.

Memoization stores already calculated states so that the same state is
not solved repeatedly.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

where `m` is the length of `s` and `n` is the length of `p`.

## Platform

LeetCode #44 - Wildcard Matching
