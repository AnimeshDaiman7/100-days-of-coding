# Day 78 - Scramble String

## Problem

Given two strings `s1` and `s2` of the same length, determine whether `s2`
is a scrambled string of `s1`.

A string can be scrambled by recursively dividing it into two non-empty
substrings and either keeping the two parts in the same order or swapping
them.

Return `true` if `s2` can be obtained from `s1` through such scrambling,
otherwise return `false`.

### Example

Input:

s1 = "great"
s2 = "rgeat"

Output:

true

## Approach

The solution uses Dynamic Programming with recursion.

- Divide `s1` into two parts at every possible position.
- Let the parts be `x` and `y`.
- There are two possibilities:
  - Keep the order: `x + y`
  - Swap the order: `y + x`
- Recursively check whether the corresponding parts of `s2`
  are scrambles of the two parts.
- If any split produces a valid result, return `true`.
- Memoization is used to store already solved substring combinations
  and avoid repeated calculations.

Before performing recursive checks, the character frequencies can also
be compared. If the two substrings do not contain the same characters,
they cannot be scrambles.

## Complexity

- Time Complexity: O(n^4) with memoization and substring checks.
- Space Complexity: O(n^3) for the DP states.

## Platform

LeetCode #87 - Scramble String
