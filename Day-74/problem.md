# Day 74 - Palindrome Partitioning II

## Problem

Given a string `s`, partition `s` such that every substring of the partition
is a palindrome.

Return the minimum number of cuts needed for a palindrome partitioning of `s`.

### Example

Input:

s = "aab"

Output:

1

Explanation:

The palindrome partitioning ["aa", "b"] can be produced using 1 cut.

## Approach

The solution uses Dynamic Programming.

First, create a DP table `pal` where:

`pal[i][j]` tells whether the substring `s[i:j+1]` is a palindrome.

A substring is a palindrome when:

- The characters at both ends are equal.
- The substring between them is also a palindrome.

Then create a `cuts` array where `cuts[i]` represents the minimum number
of cuts needed to partition the substring `s[0:i+1]` into palindromes.

For every position:

- Check all possible starting positions.
- If the substring is a palindrome, update the minimum cuts.
- If the palindrome starts from index 0, no cut is required.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(n²)

## Platform

LeetCode #132 - Palindrome Partitioning II
