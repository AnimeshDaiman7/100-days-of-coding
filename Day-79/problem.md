# Day 79 - Substring with Concatenation of All Words

## Problem

Given a string `s` and an array of strings `words`, where all words have
the same length, return the starting indices of all substrings of `s`
that are concatenations of every word in `words` exactly once.

The words can appear in any order.

### Example

Input:

s = "barfoothefoobarman"
words = ["foo","bar"]

Output:

[0,9]

Explanation:

The substring starting at index `0` is `"barfoo"`, which is a
concatenation of `"bar"` and `"foo"`.

The substring starting at index `9` is `"foobar"`, which is also a
concatenation of the two words.

## Approach

The solution uses Sliding Window and Hash Maps.

- Store the frequency of every word in `words`.
- Calculate the length of each word and the total required window size.
- Start the sliding window from every possible offset from `0` to
  `word_length - 1`.
- Read the string in chunks of `word_length`.
- If the current word is not present in the required word frequency map,
  reset the current window.
- If the current word appears more times than allowed, move the left
  pointer forward until the frequency becomes valid again.
- When the window contains all required words, add its starting index
  to the result.

## Complexity

- Time Complexity: O(n), where `n` is the length of `s`.
- Space Complexity: O(k), where `k` is the number of distinct words.

## Platform

LeetCode #30 - Substring with Concatenation of All Words
