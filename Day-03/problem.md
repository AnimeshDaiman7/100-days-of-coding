# Day 3 - Group Anagrams

## Problem

Given an array of strings strs, group the anagrams together.

### Example

Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[["bat"],["nat","tan"],["ate","eat","tea"]]

## Approach

- Sort each string.
- Use the sorted string as a key in a dictionary.
- Store all strings with the same sorted representation in the same group.

## Complexity

- Time Complexity: O(n × k log k)
- Space Complexity: O(n × k)

## Platform

LeetCode #49 - Group Anagrams
