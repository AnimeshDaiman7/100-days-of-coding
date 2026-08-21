# Day 82 - Text Justification

## Problem

Given an array of strings `words` and an integer `maxWidth`, format the text
such that each line has exactly `maxWidth` characters and is fully
left and right justified.

Words should be packed using a greedy approach, meaning we should fit as
many words as possible into each line.

Extra spaces between words should be distributed as evenly as possible.
If the spaces cannot be divided equally, the gaps on the left should receive
more spaces.

The last line should be left-justified with a single space between words.

### Example

Input:

words = ["This","is","an","example","of","text","justification."]
maxWidth = 16

Output:

[
    "This    is    an",
    "example  of text",
    "justification.  "
]

## Approach

- Start from the first word and greedily add as many words as possible
  to the current line.
- Calculate the total number of spaces required to make the line exactly
  `maxWidth` characters.
- For normal lines:
  - Divide the extra spaces among the gaps.
  - Give the left gaps one additional space when the spaces are not
    evenly divisible.
- For a line containing only one word, add all remaining spaces at the end.
- For the last line, join words using one space and pad the remaining
  spaces at the end.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

where `n` is the total number of characters/words processed.

## Platform

LeetCode #68 - Text Justification
