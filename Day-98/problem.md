# Day 98 - Word Break II

## Problem

Given a string `s` and a dictionary of strings `wordDict`, add spaces in
`s` to construct a sentence where each word is a valid dictionary word.

Return all possible sentences in any order.

The same word in the dictionary may be reused multiple times.

## Example

Input:

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

Output:

["cats and dog","cat sand dog"]

## Approach

- Use DFS to explore all possible word breaks.
- Start from index `0`.
- Try every substring starting from the current index.
- If the substring is present in `wordDict`, recursively solve the
  remaining part of the string.
- Add the current word to every valid sentence from the remaining part.
- Use memoization to avoid solving the same suffix repeatedly.

## Complexity

- Time Complexity: Depends on the number of valid sentences.
- Space Complexity: O(n), excluding the output.

## Platform

LeetCode #140 - Word Break II
