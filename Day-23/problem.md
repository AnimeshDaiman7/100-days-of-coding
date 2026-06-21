# Day 23 - Ransom Note

## Problem

Given two strings ransomNote and magazine, return true if ransomNote can be constructed using the letters from magazine.

Each letter in magazine can only be used once.

### Example

Input:

ransomNote = "aa"
magazine = "aab"

Output:

true

## Approach

- Count frequencies of characters in magazine.
- Traverse ransomNote.
- If a required character is unavailable, return false.
- Otherwise use that character and continue.

## Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(1)

## Platform

LeetCode #383 - Ransom Note
